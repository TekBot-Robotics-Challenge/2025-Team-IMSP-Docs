import cv2
import numpy as np
import os
import yaml
import ast
from pyzbar.pyzbar import decode

# --- Variables globales ---
FICHIER_YML = "quartiers.yml"
dernier_qr_data = None

# --- Fonctions ---
def detect_qr(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Simplified detection based on reference - complex filtering can interfere with some cameras
    return decode(gray)
    
    # rgb = cv2.GaussianBlur(gray, (5, 5), 0)
    # rgb = cv2.adaptiveThreshold(
    #     gray, 255,
    #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #     cv2.THRESH_BINARY, 31, 3
    # )
    # rgb = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # return decode(rgb)



TABLEAU_QUARTIERS = []


def ajouter_qr_data(qr_data):
    global TABLEAU_QUARTIERS

    # Cas "quartier bonus"
    if qr_data == "quartier bonus":
        nouveau_dico = {
            "nom_du_quartier": qr_data,
            "nombre_de_point_total_de_collecte": 50
        }

    else:
        try:
            qr_dict = ast.literal_eval(qr_data)
        except Exception as e:
            print("QR Python dict invalide :", e)
            return

        # Vérification des clés
        if "nom" not in qr_dict or "pts_collecte" not in qr_dict:
            print("Erreur : clés 'nom' ou 'pts_collecte' manquantes dans le QR")
            return

        nouveau_dico = {
            "nom_du_quartier": qr_dict["nom"],
            "nombre_de_point_total_de_collecte": int(qr_dict["pts_collecte"])
        }

    # Vérification des doublons
    for d in TABLEAU_QUARTIERS:
        if (d["nom_du_quartier"] == nouveau_dico["nom_du_quartier"] and
            int(d["nombre_de_point_total_de_collecte"]) == nouveau_dico["nombre_de_point_total_de_collecte"]):
            print("Quartier déjà présent → ignoré")
            return

    # Ajouter et trier
    TABLEAU_QUARTIERS.append(nouveau_dico)

    TABLEAU_QUARTIERS.sort(
        key=lambda d: d["nombre_de_point_total_de_collecte"],
        reverse=True
    )

    print(f"Quartier ajouté : {nouveau_dico['nom_du_quartier']}")

# def draw_qr(frame, qr_objects):
#     global dernier_qr_data
#     for qr in qr_objects:
#         text = qr.data.decode("utf-8")
#         ajouter_qr_data(text)

#         pts = np.array(qr.polygon, np.int32)
#         pts = pts.reshape((-1, 1, 2))

#         cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
#         cv2.putText(
#             frame,
#             text,
#             (pts[0][0][0], pts[0][0][1] - 10),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.7,
#             (0, 255, 0),
#             2
#         )

#     return frame
