#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import cv2
import time
# Assuming qr_lib is in the x3_control package
from x3_control import qr_lib

class QRServiceNode(Node):
    def __init__(self):
        super().__init__('qr_service_node')
        self.srv = self.create_service(Trigger, 'scan_qr', self.scan_callback)
        self.get_logger().info("QR Service Node Started")

    def scan_callback(self, request, response):
        self.get_logger().info("Scanning for QR code...")
        
        cap = cv2.VideoCapture(0)

        # Setup settings based on Yahboom reference
        cv_edition = cv2.__version__
        if cv_edition[0] == '3': 
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'XVID'))
        else: 
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        if not cap.isOpened():
            response.success = False
            response.message = "Could not open camera"
            self.get_logger().error(response.message)
            return response

        found = False
        detected_text = ""
        
        for _ in range(40): 
            ret, frame = cap.read()
            if not ret:
                continue
            if found:
                break
                
            qr_objects = qr_lib.detect_qr(frame)
            if not qr_objects:
                print("Aucun QR code")
            else:
                for qr in qr_objects:
                    detected_text = qr.data.decode("utf-8")
                    print(f"Detected QR: {detected_text}")
                    found = True
                    break
            time.sleep(0.05)
            
        cap.release()
        
        if found:
            response.success = True
            response.message = f"QR Detected: {detected_text}"
            self.get_logger().info(response.message)
        else:
            response.success = False
            response.message = "No QR code found."
            self.get_logger().warn(response.message)
            
        return response

def main(args=None):
    rclpy.init(args=args)
    node = QRServiceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
