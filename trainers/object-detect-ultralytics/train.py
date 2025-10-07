from ultralytics import YOLO

# the base model, to use
model = YOLO("yolo11n.pt")

results = model.train(data="cops/data.yaml", epochs=5, device="mps", imgsz=640)
