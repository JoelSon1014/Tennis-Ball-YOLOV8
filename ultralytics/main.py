# Import YOLO model
from ultralytics import YOLO
import cv2 as cv

# Load a model
model = YOLO('best.pt')  # Load a pretrained model

# Predict using the model
results = model.predict("1.png")

# Assuming the first result is what we need
result = results[0]

# Accessing the original image
img = result.orig_img

# Filter and sort rocks based on the size of their bounding box
rock_boxes = [box for box in result.boxes if result.names[box.cls[0].item()] == 'rock']
rock_boxes.sort(key=lambda box: (box.xyxy[0][2] - box.xyxy[0][0]) * (box.xyxy[0][3] - box.xyxy[0][1]), reverse=True)

# Select top three largest rocks
top_3_rocks = rock_boxes[:3]

# Draw rectangle around each of the top three rocks
for box in top_3_rocks:
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]

    img = cv.rectangle(img, (cords[0], cords[1]), (cords[2], cords[3]), (255, 0, 0), 10)

# Save the image with rectangles
cv.imwrite("annotated_image.png", img)
cv.waitKey(0)
