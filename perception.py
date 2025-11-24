# perception.py
import cv2
import numpy as np
from ultralytics import YOLO
from config import YOLO_MODEL, ROI

model = YOLO(YOLO_MODEL)

def point_in_poly(pt, poly):
    return cv2.pointPolygonTest(np.array(poly, np.int32), pt, False) >= 0

def get_vehicle_count(frame):
    result = model(frame, stream=False)[0]
    count = 0

    for box in result.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        if cls_name.lower() not in ["car", "bus", "truck", "motorbike"]:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cx, cy = (x1 + x2)//2, (y1 + y2)//2

        if point_in_poly((cx, cy), ROI):
            count += 1

    return count