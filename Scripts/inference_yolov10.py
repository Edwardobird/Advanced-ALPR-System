from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('jameslahm/yolov10n')
source = 'http://images.cocodataset.org/val2017/000000039769.jpg'
model.predict(source=source, save=True)

from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('path/to/your/trained/model.pt')
source = 'path/to/test/image.jpg'
model.predict(source=source, save=True)
