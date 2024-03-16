# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# # To detect face -> pre-trained face detection model
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # List of authorized users


# while True:

#     ret, frame = cap.read()

#     # Convert the frame to grayscale 
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# ********************
# import face_recognition
# import os, sys 
# import cv2
# import numpy as np
# import math

# def face_confidence(face_distance, face_match_threshold = 0.6):
#     range = (1.0 - face_match_threshold)
#     linear_val = (1.0 - face_distance) / (range * 2.0)

#     if(face_distance > face_match_threshold):
#         return str(round(linear_val * 100 , 2)) + '%'
#     else:
#         value = (linear_val + ((1.0 - linear_val) *  math.pow((linear_val - 0.5) * 2))) * 100
#         return str(round(value, 2)) + '%'
    

# class FaceRecognition:
#     face_location = []
#     face_encodings = []
#     face_name = []
#     known_face_encodings = []
#     known_face_names = []
#     process_current_frame = True


#     def __init__(self):
#         self.encode_faces()
        
    
#     def encode_faces(self):
#         for image in os.listdir('images'):
#             face_image = face_recognition.load_image_file(f'images/{image}')
#             face_encoding =  face_recognition.face_encodings(face_image)[0]

#             self.known_face_encodings.append(face_encoding)
#             self.known_face_names.append(image)
        
#         print(self.known_face_names)
    
#     def run_recognition(self):
#         video_capture = cv2.VideoCapture(0)

#         if not video_capture.isOpened():
#             sys.exit('Video source is not found...')

#         while True:
#             ret , frame = video_capture.read()

#             if self.process_current_frame:
#                 small_frame = cv2.resize(frame , (0,0) , fx = 0.25 , fy = 0.25)
#                 rgb_small_frame = small_frame[ :, :, ::-1]

#                 # Find all the faces
#                 self.face_location = face_recognition.face_locations(rgb_small_frame)
#                 self.face_encodings = face_recognition.face_encodings(rgb_small_frame ,self.face_location)

#                 self.face_names = []
#                 for face_encoding in self.face_encodings:
#                     matches = face_recognition.compare_faces(self.known_face_encodings , face_encoding)
#                     name = 'Unkown'
#                     confidence = 'Unkown'

#                     face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances)

#                     if matches[best_match_index]:
#                         name = self.known_face_names[best_match_index]
#                         confidence = face_confidence(face_distances[best_match_index])
                    
#                     self.face_names(f'{name} ({confidence})')
            
#             self.process_current_frame = not self.process_current_frame


#             # Display anotation
#             for(top , right , bottom , left), name in zip(self.face_location , self.face_names):
#                 top *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4

#                 cv2.rectangle(frame , (left,top) , (right , bottom) , (0,0,255), 2)
#                 cv2.rectangle(frame , (left,bottom - 35) , (right , bottom) , (0,0,255), -1)
#                 cv2.putText(frame, name, (left + 6 , bottom - 6), cv2.FONT_HERSHEY_DUPLEX , 0.8 , (255,255,255) , 1)

            
#             cv2.imshow('Face Recognition' , frame)

#             if cv2.waitKey(1) == ord('q'):
#                 break
        
#         video_capture.release()
#         cv2.destroyAllWindows()

# if __name__ == '__main__':
#     fr = FaceRecognition()
#     fr.run_recognition()


# import cv2
# import pymongo

# # Load the pre-trained face detection model
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Function to authenticate users by comparing faces with enrolled data
# def authenticate_user(frame, collection):
#     client = pymongo.MongoClient("mongodb+srv://nishant123:nishant123@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority&appName=firstproject")
#     db = client["facial_recognition"]
#     authorized_faces = db[collection]

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     for (x, y, w, h) in faces:
#         face_roi = gray[y:y+h, x:x+w]
#         for enrolled_face in authorized_faces.find():
#             # Compare faces using some similarity metric (e.g., histogram comparison, deep learning-based face recognition)
#             # Here, we are using simple histogram comparison as an example
#             similarity = cv2.compareHist(cv2.calcHist([face_roi], [0], None, [256], [0, 256]),
#                                           cv2.calcHist([enrolled_face['face']], [0], None, [256], [0, 256]), cv2.HISTCMP_CORREL)
#             if similarity > 0.7:  # Adjust this threshold based on your requirement
#                 return True
#     return False

# # Initialize video capture
# cap = cv2.VideoCapture(0)

# # Authentication Phase
# print("Authentication phase - Showing your face will authenticate you.")
# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     for (x, y, w, h) in faces:
#          cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     if authenticate_user(frame, "authorized_users"):
#         print('Authorized')
#     else:
#         print('Unauthorized')

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# while True:

#     ret, frame = cap.read()

#     # Convert the frame to grayscale 
#     

#     # Detect faces in the frame
#     
#     # Draw rectangles around the detected faces
#     

#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1) == ord('q'):
#         break
# Release the video capture and close all windows


# *************************

import cv2
import os

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load enrolled face images from the local folder
enrolled_faces_dir = "face_data/"
enrolled_faces = []
for filename in os.listdir(enrolled_faces_dir):
    if filename.endswith(".jpg"):
        enrolled_face_path = os.path.join(enrolled_faces_dir, filename)
        enrolled_face_img = cv2.imread(enrolled_face_path)
        enrolled_faces.append(enrolled_face_img)

# Function to perform facial recognition
def recognize_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]

        # Compare faces with enrolled faces
        for enrolled_face in enrolled_faces:
            # Compare faces using some similarity metric (e.g., histogram comparison, deep learning-based face recognition)
            # Here, we are using simple histogram comparison as an example
            similarity = cv2.compareHist(cv2.calcHist([face_roi], [0], None, [256], [0, 256]),
                                         cv2.calcHist([enrolled_face], [0], None, [256], [0, 256]), cv2.HISTCMP_CORREL)
            if similarity > 0.7:  # Adjust this threshold based on your requirement
                return True

    return False

# Initialize video capture
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

# Authentication Phase
print("Authentication phase - Showing your face will authenticate you.")
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Perform facial recognition
    authorized = recognize_face(frame)

    # Display authentication status on the frame
    status_text = "Authorized" if authorized else "Unauthorized"
    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if authorized else (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

