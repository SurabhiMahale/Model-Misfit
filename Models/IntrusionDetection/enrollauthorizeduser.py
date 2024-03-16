import cv2
import pymongo

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to enroll authorized users and store data in MongoDB
def enroll_user(image_path, collection):
    client = pymongo.MongoClient("mongodb+srv://nishant123:nishant123@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority&appName=firstproject")
    db = client["facial_recognition"]
    authorized_faces = db[collection]

    image = cv2.imread(image_path)
    gray = cv2.imread(image_path)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        face_data = {'image_path': image_path, 'face': gray[y:y+h, x:x+w].tolist()}
        authorized_faces.insert_one(face_data)

    print(face_data)

# Enrollment Phase - Load and store authorized users' faces in MongoDB
authorized_images = ['images/faceNishant.png']

# img = ("/images/faceNishant.png")
# enroll_user(img,"authorized_users")

for image_path in authorized_images:
    enroll_user(image_path, "authorized_users")
