from ultralytics import YOLO


model = YOLO("best220.pt")

results = model.predict(source="0", show=True) 

print(results)