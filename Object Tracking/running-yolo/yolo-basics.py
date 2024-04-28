
from ultralytics import YOLO
import cv2
model = YOLO('../Yolo-weights/yolov8l.pt')
result = model(r'C:\Users\ASUS\Desktop\Machine Learning\pythonProject\Images\2.jpg', show = True)
cv2.waitKey(0)