import cv2
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
import threading

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load enrolled face images from the local folder
enrolled_faces_dir = "face_data/"
enrolled_faces_features = []

def extract_features(face_img):
    # Load the VGG16 model pre-trained on ImageNet
    model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    # Resize the face image to match the input size of the VGG16 model
    resized_img = cv2.resize(face_img, (224, 224))
    
    # Convert the BGR image to RGB
    resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    
    # Convert the image to an array
    img_array = image.img_to_array(resized_img)
    
    # Expand the dimensions to create a batch of size 1
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess the input image
    preprocessed_img = preprocess_input(img_array)
    
    # Extract features using the pre-trained VGG16 model
    features = model.predict(preprocessed_img)
    
    # Flatten the features
    features = features.flatten()
    
    return features
# Load enrolled face features
for filename in os.listdir(enrolled_faces_dir):
    if filename.endswith(".jpg"):
        enrolled_face_path = os.path.join(enrolled_faces_dir, filename)
        enrolled_face_img = cv2.imread(enrolled_face_path)
        enrolled_face_feature = extract_features(enrolled_face_img)
        enrolled_faces_features.append(enrolled_face_feature)

# Function to extract features from a face image


# Function to perform facial recognition using cosine similarity
def recognize_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        detected_face_feature = extract_features(frame[y:y+h, x:x+w])
        
        # Compare features with enrolled faces
        for enrolled_face_feature in enrolled_faces_features:
            similarity_score = cosine_similarity([detected_face_feature], [enrolled_face_feature])[0][0]
            if similarity_score > 0.7:  # Adjust this threshold based on your requirement
                return True
    
    return False

# Function to process frames from video capture
def process_frames():
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

        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Perform facial recognition
        authorized = recognize_face(frame)

        # Display authentication status on the frame
        status_text = "Authorized" if authorized else "Unauthorized"
        cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if authorized else (0, 0, 255), 2)

        try:
            # Display the frame
            cv2.imshow("Face Recognition", frame)
        except Exception as e:
            print("Error:", e)

        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Start a separate thread for processing frames
frame_thread = threading.Thread(target=process_frames)
frame_thread.start()
