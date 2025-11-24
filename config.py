# config.py

YOLO_MODEL = "yolov8n.pt"
CAMERA_SOURCE = 0  # webcam or video file

# ROI polygon for the lane (tune based on camera)
ROI = [(100,400), (1180,400), (1180,600), (100,600)]

# Logic Settings
EXTEND_THRESHOLD = 10
EXTEND_SECONDS = 5
DEFAULT_GREEN = 15
MAX_GREEN = 30
CHECK_INTERVAL = 2.0