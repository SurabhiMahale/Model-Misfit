# import cv2
# import os

# # Load the pre-trained face detection model
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Load enrolled face images from the local folder
# enrolled_faces_dir = "face_data/"
# enrolled_faces = []
# for filename in os.listdir(enrolled_faces_dir):
#     if filename.endswith(".jpg"):
#         enrolled_face_path = os.path.join(enrolled_faces_dir, filename)
#         enrolled_face_img = cv2.imread(enrolled_face_path)
#         enrolled_faces.append(enrolled_face_img)

# # Function to perform facial recognition
# def recognize_face(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     for (x, y, w, h) in faces:
#         face_roi = gray[y:y+h, x:x+w]

#         # Compare faces with enrolled faces
#         for enrolled_face in enrolled_faces:
#             # Compare faces using some similarity metric (e.g., histogram comparison, deep learning-based face recognition)
#             # Here, we are using simple histogram comparison as an example
#             similarity = cv2.compareHist(cv2.calcHist([face_roi], [0], None, [256], [0, 256]),
#                                          cv2.calcHist([enrolled_face], [0], None, [256], [0, 256]), cv2.HISTCMP_CORREL)
#             if similarity > 0.7:  # Adjust this threshold based on your requirement
#                 return True

#     return False

# # Initialize video capture
# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Error: Unable to open camera.")
#     exit()

# # Authentication Phase
# print("Authentication phase - Showing your face will authenticate you.")
# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     # Perform facial recognition
#     authorized = recognize_face(frame)

#     # Display authentication status on the frame
#     status_text = "Authorized" if authorized else "Unauthorized"
#     cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if authorized else (0, 0, 255), 2)

#     # Display the frame
#     cv2.imshow("Face Recognition", frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the video capture and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import face_recognition
import os

# Load known faces
known_faces_path = "/kaggle/input/face-sample/known faces"
known_faces = []
faceList = ["Kenneth"]

# Iterate through files in the "known_faces" folder
for filename in os.listdir(known_faces_path):
    image_path = os.path.join(known_faces_path, filename)
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)

# Open the video file
video_file = "https://res.cloudinary.com/dp0ayty6p/video/upload/v1705433352/samples/FACESAMPLEvid.mp4"
video_capture = cv2.VideoCapture(video_file)

# Get video properties
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_file = "output_video.mp4"
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

while True:
    # Capture each frame from the video feed
    ret, frame = video_capture.read()

    # Break the loop if the video is over
    if not ret:
        break

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the first known face
        if True in matches:
            first_match_index = matches.index(True)
            name = faceList[first_match_index]
            label_color = (0, 255, 0)  # Authorized faces are green
        else:
            label_color = (0, 0, 255)  # Unauthorized faces are red

        # Draw a rectangle around the face and display the name with label color
        cv2.rectangle(frame, (left, top), (right, bottom), label_color, 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, label_color, 1)

    # Write the frame to the output video file
    video_writer.write(frame)

# Release the video capture, writer, and close all windows
video_capture.release()
video_writer.release()
cv2.destroyAllWindows()
