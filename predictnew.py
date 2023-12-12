from ultralytics import YOLO

model = YOLO("./runs/detect/train5/weights/last.pt")

results = model.predict(source="./bins")
print(results)