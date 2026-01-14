#!/usr/bin/env python3

"""QR scanning service node.

Provides a std_srvs/Trigger service `/scan_qr` which captures a single image
from a configured camera, detects QR codes, writes results into
`quartiers.yml` (same behavior as your original script) and returns the
concatenated detected texts in `response.message`.

Parameters
- camera_index (int): default 1
- show_window (bool): default False
- quartiers_file (string): output YAML file (default: quartiers.yml)

Dependencies: opencv-python, numpy, pyzbar, pyyaml
"""

import time
import os
import ast

try:
    import cv2
    import numpy as np
    from pyzbar.pyzbar import decode
    import yaml
except Exception as e:
    # We'll still be importable; runtime failures will be logged
    cv2 = None
    np = None
    decode = None
    yaml = None

import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


# ----- QR helper functions (adapted from your script) -----

def detect_qr(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 3
    )
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    return decode(gray)


def ajouter_qr_data(qr_data, fichier_yml="quartiers.yml"):
    # Cas : QR contient un dictionnaire Python
    if qr_data != "quartier bonus":
        try:
            qr_dict = ast.literal_eval(qr_data)
        except Exception as e:
            print("❌ QR Python dict invalide :", e)
            return

        nouveau_dico = {
            "nom_du_quartier": qr_dict["nom_du_quartier"],
            "nombre_de_point_total_de_collecte": int(qr_dict["nombre_de_point_total_de_collecte"])
        }
    else:
        # Cas : QR simple (nom du quartier)
        nouveau_dico = {
            "nom_du_quartier": qr_data,
            "nombre_de_point_total_de_collecte": 50
        }

    if os.path.exists(fichier_yml):
        with open(fichier_yml, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
    else:
        data = []

    if len(data) != 0:
        for d in data:
            d["nombre_de_point_total_de_collecte"] = int(d["nombre_de_point_total_de_collecte"])

        for d in data:
            if (
                nouveau_dico["nom_du_quartier"] == d["nom_du_quartier"] and
                nouveau_dico["nombre_de_point_total_de_collecte"] == int(d["nombre_de_point_total_de_collecte"])
            ):
                print("🔁 Quartier déjà présent dans le fichier → ignoré")
                return

    data.append(nouveau_dico)

    data.sort(
        key=lambda d: d["nombre_de_point_total_de_collecte"],
        reverse=True
    )

    with open(fichier_yml, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False
        )

    print("Quartier ajouté et fichier trié")


def draw_qr_on_frame(frame, qr_objects):
    for qr in qr_objects:
        text = qr.data.decode("utf-8")
        pts = np.array(qr.polygon, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
        cv2.putText(
            frame,
            text,
            (pts[0][0][0], pts[0][0][1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
    return frame


class QRServiceNode(Node):
    def __init__(self):
        super().__init__("qr_service_node")
        self.declare_parameter("camera_index", 1)
        self.declare_parameter("show_window", False)
        self.declare_parameter("quartiers_file", "quartiers.yml")

        self.camera_index = self.get_parameter("camera_index").get_parameter_value().integer_value
        self.show_window = self.get_parameter("show_window").get_parameter_value().bool_value
        self.quartiers_file = self.get_parameter("quartiers_file").get_parameter_value().string_value

        if cv2 is None:
            self.get_logger().error("OpenCV/pyzbar not available. Install dependencies before running this node.")
            raise RuntimeError("Missing image processing dependencies")

        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        try:
            self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
        except Exception:
            pass

        self.srv = self.create_service(Trigger, "scan_qr", self.scan_callback)
        self.get_logger().info("QR scan service ready: /scan_qr")

    def scan_callback(self, request, response):
        ret, frame = self.cap.read()
        if not ret:
            response.success = False
            response.message = "camera read error"
            self.get_logger().error("Could not read from camera")
            return response

        qr_objects = detect_qr(frame)
        if not qr_objects:
            response.success = False
            response.message = "no_qr"
            self.get_logger().info("No QR code detected")
        else:
            texts = []
            for qr in qr_objects:
                text = qr.data.decode("utf-8")
                texts.append(text)
                try:
                    ajouter_qr_data(text, self.quartiers_file)
                except Exception as e:
                    self.get_logger().warning(f"Failed to add QR data: {e}")

            response.success = True
            response.message = ",".join(texts)
            self.get_logger().info(f"Detected {len(texts)} QR(s): {response.message}")

        if self.show_window:
            frame = draw_qr_on_frame(frame, qr_objects)
            cv2.imshow("QR Scanner", frame)
            cv2.waitKey(1)

        return response

    def destroy_node(self):
        try:
            if hasattr(self, "cap") and self.cap is not None:
                self.cap.release()
        except Exception:
            pass
        try:
            cv2.destroyAllWindows()
        except Exception:
            pass
        super().destroy_node()


def main():
    rclpy.init()
    node = QRServiceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
