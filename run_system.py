# run_system.py
import cv2
import time
from perception import get_vehicle_count
from controller import LogicEngine
from hardware_interface import HardwareInterface
from logger import init_db, log_event
from config import CAMERA_SOURCE, CHECK_INTERVAL, ROI
import numpy as np

def draw_roi(frame):
    cv2.polylines(frame, [np.array(ROI, np.int32)], True, (0,255,0), 2)
    return frame

def main():
    init_db()
    logic = LogicEngine()
    hardware = HardwareInterface()
    cap = cv2.VideoCapture(CAMERA_SOURCE)

    last_check = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = draw_roi(frame)

        vehicle_count = get_vehicle_count(frame)

        cv2.putText(frame, f"Count: {vehicle_count}", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)

        if time.time() - last_check >= CHECK_INTERVAL:
            last_check = time.time()

            decision = logic.decide(vehicle_count)
            log_event(vehicle_count, decision["action"], decision["duration"])
            hardware.send_command(str(decision))

        cv2.imshow("Green Light MVP", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "_main_":
    main()