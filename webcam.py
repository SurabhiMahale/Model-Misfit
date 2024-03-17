# from ultralytics import YOLO
# import cv2
# import math
# import numpy as np
# import time
# import numpy as np
# import cv2
# import pygame
# import matplotlib.pyplot as plt
# import torch
# import numpy as np
# import pygame

# # Initialize pygame
# pygame.mixer.init()

# # Load siren sound
# siren_sound = pygame.mixer.Sound('police-6007.mp3')

# # Video capturing starts
# def tampering(frame):
#     fgbg = cv2.createBackgroundSubtractorMOG2()
#     fgmask = fgbg.apply(frame)
#     kernel = np.ones((5, 5), np.uint8)
    
#     if frame is None:
#         print("End of frame")
#     else:
#         a = 0
#         bounding_rect = []
#         fgmask = fgbg.apply(frame)
#         fgmask = cv2.erode(fgmask, kernel, iterations=5) 
#         fgmask = cv2.dilate(fgmask, kernel, iterations=5)
#         contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         for i in range(len(contours)):
#             bounding_rect.append(cv2.boundingRect(contours[i]))
#         for i in range(len(contours)):
#             if bounding_rect[i][2] >= 40 or bounding_rect[i][3] >= 40:
#                 a = a + (bounding_rect[i][2]) * bounding_rect[i][3]
#             if a >= int(frame.shape[0]) * int(frame.shape[1]) / 3:
#                 cv2.putText(frame, "TAMPERING DETECTED", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
#                 # Play siren sound
#                 siren_sound.play()
#         cv2.imshow('frame', frame)

# # Load your custom models
# generic_model = YOLO("yolov8n.pt")
# fire_model = YOLO("Models/Fire Detection/fire.pt")
# violence_model = YOLO("Models/Violence Detection/ViolenceDet.pt")
# weapons_model = YOLO("Models/weapon Detection/best.pt")

# # Define classes and model mapping
# classes = {
#     "generic": ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"
#               ],
#     "fire": ["fire", "smoke"],
#     "violence": ["violence", "weapons"]
# }

# # Initialize video capture
# cap = cv2.VideoCapture(0)  # Use camera index 0 (default webcam)

# # Main loop for real-time analysis
# while True:
#     ret, frame = cap.read()  # Read frame from the video capture
#     if not ret:
#         print("Error: Unable to capture frame")
#         break
    
#     # Perform analysis with fire detection model
#     fire_results = fire_model(frame)
#     # Process fire detection results (draw bounding boxes, etc.)

#     # Perform analysis with violence detection model
#     violence_results = violence_model(frame)
#     # Process violence detection results (draw bounding boxes, etc.)
#     weapons_results = weapons_model(frame)
#     # Process weapons detection results (draw bounding boxes, etc.)
#     generic_results = generic_model(frame)
#     # Detect tampering
#     tampering(frame)

#     # Display the processed frame with detections
#     cv2.imshow("Real-Time Analysis", frame)

#     # Check for key press to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release video capture object and close windows
# cap.release()
# cv2.destroyAllWindows()




# from ultralytics import YOLO
# import cv2
# import numpy as np
# import time
# import pygame  # For audio alerts (optional)

# # Initialize pygame for audio alerts (uncomment if using)
# # pygame.mixer.init()
# # siren_sound = pygame.mixer.Sound('police-6007.mp3')

# # Video capturing starts
# def tampering(frame):
#     fgbg = cv2.createBackgroundSubtractorMOG2()
#     fgmask = fgbg.apply(frame)
#     kernel = np.ones((5, 5), np.uint8)

#     if frame is None:
#         print("End of frame")
#     else:
#         bounding_rect = []
#         a = 0

#         fgmask = fgbg.apply(frame)
#         fgmask = cv2.erode(fgmask, kernel, iterations=5)
#         fgmask = cv2.dilate(fgmask, kernel, iterations=5)
#         contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#         for i in range(len(contours)):
#             bounding_rect.append(cv2.boundingRect(contours[i]))
#             x, y, w, h = bounding_rect[i]

#             # Draw rectangle and label with area
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             area = w * h
#             text = f"Area: {area}"
#             cv2.putText(frame, text, (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

#             # Tampering detection logic (adjust threshold as needed)
#             if area >= int(frame.shape[0]) * int(frame.shape[1]) / 3:
#                 cv2.putText(frame, "TAMPERING DETECTED", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#                 # Play siren sound (uncomment if using pygame)
#                 # siren_sound.play()

#         cv2.imshow('frame', frame)

# # Load your custom models
# generic_model = YOLO("yolov8n.pt")  # Generic object detection
# fire_model = YOLO("Models/Fire Detection/fire.pt")  # Fire detection
# violence_model = YOLO("Models/Violence Detection/ViolenceDet.pt")  # Violence detection
# weapons_model = YOLO("Models/weapon Detection/best.pt")  # Weapon detection

# # Define classes and model mapping
# classes = {
#     "generic": [
#         "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#         "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#         "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#         "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#         "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#         "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#         "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#         "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#         "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#         "teddy bear", "hair drier", "toothbrush"
#     ],
#     "fire": ["fire", "smoke"],
#     "violence": ["violence", "weapons"]
# }

# # Initialize video capture
# cap = cv2.VideoCapture(0)  # Use camera

# # Main loop for real-time analysis
# while True:
#     ret, frame = cap.read()  # Read frame from the video capture
#     if not ret:
#         print("Error: Unable to capture frame")
#         break

#     # Perform analysis with fire detection model
#     fire_results = fire_model(frame)
#     # Process fire detection results (draw bounding boxes, etc.)
#     with open('detection_results.txt', 'a') as f:
#         f.write("Fire Detection Results:\n")
#         if fire_results:
#             for result in fire_results.xyxy[0]:
#                 f.write(f"Class: {classes['fire'][int(result[5])]}, Confidence: {result[4]}\n")
#         else:
#             f.write("No fire detected\n")

#     # Perform analysis with violence detection model
#     violence_results = violence_model(frame)
#     # Process violence detection results (draw bounding boxes, etc.)
#     with open('detection_results.txt', 'a') as f:
#         f.write("Violence Detection Results:\n")
#         if violence_results:
#             for result in violence_results.xyxy[0]:
#                 f.write(f"Class: {classes['violence'][int(result[5])]}, Confidence: {result[4]}\n")
#         else:
#             f.write("No violence detected\n")

#     # Perform analysis with weapons detection model
#     weapons_results = weapons_model(frame)
#     # Process weapons detection results (draw bounding boxes, etc.)
#     with open('detection_results.txt', 'a') as f:
#         f.write("Weapons Detection Results:\n")
#         if weapons_results:
#             for result in weapons_results.xyxy[0]:
#                 f.write(f"Class: {classes['generic'][int(result[5])]}, Confidence: {result[4]}\n")
#         else:
#             f.write("No weapons detected\n")

#     # Perform analysis with generic object detection model
#     generic_results = generic_model(frame)
#     # Process generic object detection results (draw bounding boxes, etc.)
#     with open('detection_results.txt', 'a') as f:
#         f.write("Generic Object Detection Results:\n")
#         if generic_results:
#             for result in generic_results.xyxy[0]:
#                 f.write(f"Class: {classes['generic'][int(result[5])]}, Confidence: {result[4]}\n")
#         else:
#             f.write("No objects detected\n")

#     # Detect tampering
#     tampering(frame)

#     # Display the processed frame with detections
#     cv2.imshow("Real-Time Analysis", frame)

#     # Check for key press to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release video capture object and close windows
# cap.release()

# cv2.destroyAllWindows()


# from ultralytics import YOLO
# import cv2

# # Initialize your custom models
# fire_model = YOLO("Models/Fire Detection/fire.pt")
# violence_model = YOLO("Models/Violence Detection/ViolenceDet.pt")
# weapons_model = YOLO("Models/weapon Detection/best.pt")
# generic_model = YOLO("yolov8n.pt")

# # Define classes for each model
# classes = {
#     "fire": ["fire", "smoke"],
#     "violence": ["violence", "weapons"],
#     "weapons": ["weapon"],
#     "generic": ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#                 "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#                 "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#                 "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#                 "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#                 "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#                 "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#                 "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#                 "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#                 "teddy bear", "hair drier", "toothbrush"
#                 ]
# }

# # Function to draw bounding boxes and labels on the image
# def draw_boxes(img, boxes, class_names, color=(0, 255, 0), thickness=2):
#     for box in boxes:
#         x, y, w, h, conf, cls = box
#         class_name = class_names[int(cls)]
#         cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), color, thickness)
#         cv2.putText(img, class_name, (int(x - w / 2), int(y - h / 2 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

# # Initialize video capture
# cap = cv2.VideoCapture(0)  # Use camera index 0 (default webcam)

# # Main loop for real-time analysis
# while True:
#     ret, frame = cap.read()  # Read frame from the video capture
#     if not ret:
#         print("Error: Unable to capture frame")
#         break
    
#     # Perform analysis with fire detection model
#     fire_results = fire_model(frame)
#     # Process fire detection results
#     if fire_results:
#         fire_boxes = fire_results.xyxy[0].numpy()
#         draw_boxes(frame, fire_boxes, classes["fire"])
#     else:
#         print("No objects detected by fire detection model")

#     # Perform analysis with violence detection model
#     violence_results = violence_model(frame)
#     # Process violence detection results
#     if violence_results:
#         violence_boxes = violence_results.xyxy[0].numpy()
#         draw_boxes(frame, violence_boxes, classes["violence"])
#     else:
#         print("No objects detected by violence detection model")

#     # Perform analysis with weapons detection model
#     weapons_results = weapons_model(frame)
#     # Process weapons detection results
#     if weapons_results:
#         weapons_boxes = weapons_results.xyxy[0].numpy()
#         draw_boxes(frame, weapons_boxes, classes["weapons"])
#     else:
#         print("No objects detected by weapon detection model")

#     # Perform analysis with generic object detection model
#     generic_results = generic_model(frame)
#     # Process generic object detection results
#     if generic_results:
#         generic_boxes = generic_results.xyxy[0].numpy()
#         draw_boxes(frame, generic_boxes, classes["generic"])
#     else:
#         print("No objects detected by generic detection model")

#     # Display the processed frame with detections
#     cv2.imshow("Real-Time Analysis", frame)

#     # Check for key press to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release video capture object and close windows
# cap.release()
# cv2.destroyAllWindows()




from ultralytics import YOLO
import cv2

# Initialize your custom models
fire_model = YOLO("Models/Fire Detection/fire.pt")
violence_model = YOLO("Models/Violence Detection/ViolenceDet.pt")
weapons_model = YOLO("Models/weapon Detection/best.pt")
generic_model = YOLO("yolov8n.pt")

# Define classes for each model
classes = {
    "fire": ["fire", "smoke"],
    "violence": ["violence", "weapons"],
    "weapons": ["weapon"],
    "generic": ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
                "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
                "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
                "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                "teddy bear", "hair drier", "toothbrush"
                ]
}

# Function to draw bounding boxes and labels on the image
def draw_boxes(img, boxes, class_names, color=(0, 255, 0), thickness=2):
    for box in boxes:
        x, y, w, h, conf, cls = box
        class_name = class_names[int(cls)]
        cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), color, thickness)
        cv2.putText(img, class_name, (int(x - w / 2), int(y - h / 2 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use camera index 0 (default webcam)

# Main loop for real-time analysis
while True:
    ret, frame = cap.read()  # Read frame from the video capture
    if not ret:
        print("Error: Unable to capture frame")
        break
    
    # Perform analysis with fire detection model
    fire_results = fire_model(frame)
    
    # Check if fire_results is empty or a list
    if not fire_results or isinstance(fire_results, list):
        print("No objects detected by fire detection model")
        fire_boxes = []
    else:
        # Assuming the first item in the list contains the detection results
        fire_boxes = fire_results.xyxy[0].numpy()
    
    # Perform analysis with violence detection model
    violence_results = violence_model(frame)
    ...
    # Perform analysis with weapons detection model
    weapons_results = weapons_model(frame)
    ...
    # Perform analysis with generic object detection model
    generic_results = generic_model(frame)
    ...

    # Display the processed frame with detections
    cv2.imshow("Real-Time Analysis", frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close windows
cap.release()
cv2.destroyAllWindows()
