import cv2
import pymongo

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
data_dir = "face_data/"

# Function to enroll authorized users and store data in MongoDB
def enroll_user(image_path, collection, face_count):
    client = pymongo.MongoClient("mongodb+srv://nishant123:nishant123@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority&appName=firstproject")
    db = client["facial_recognition"]
    authorized_faces = db[collection]

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        for i, (x, y, w, h) in enumerate(faces):
            face_roi = gray[y:y+h, x:x+w]
            face_data = {'image_path': f"{data_dir}face_{face_count + i}.jpg", 'face': face_roi.tolist()}
            cv2.imwrite(f"{data_dir}face_{face_count + i}.jpg", face_roi)
            print("Face data saved:", face_data['image_path'])
        
        return face_count + len(faces)
    else:
        return face_count

# Enrollment Phase - Load and store authorized users' faces in MongoDB
authorized_images = ['images/faceNitesh.png','images/faceNishant.png']
face_count = 0

for image_path in authorized_images:
    face_count = enroll_user(image_path, "authorized_users", face_count)
