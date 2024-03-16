from flask import Flask, request, jsonify
import numpy as np
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_cors import CORS
from object_detection_model import ObjectDetection  # Assuming you have a custom model

app = Flask(__name__)
CORS(app)
detector = ObjectDetection(capture_index=0)

# Load known faces
known_faces = {
    "authorized_user1": "nishant.jpg",
    "authorized_user2": "nitesh.jpg",
    "authorized_user3": "devang.jpg",
    # Add more authorized users as needed
}

# Email configuration
password = "gnpi egai czue lohr"
from_email = "niteshbrathod14@gmail.com"
to_email = "niteshbrathod1432003@gmail.com"
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_email, password)

def recognize_face(face_encoding):
    for name, known_image_path in known_faces.items():
        known_image = cv2.imread(known_image_path)
        known_encoding = face_recognition.face_encodings(known_image)[0]
        match = face_recognition.compare_faces([known_encoding], face_encoding)
        if match[0]:
            return name
    return "Unknown"

def send_email(object_detected):
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = "Security Alert"
    message_body = f'ALERT - {object_detected} unknown person detected!!'
    message.attach(MIMEText(message_body, 'plain'))
    server.sendmail(from_email, to_email, message.as_string())

@app.route('/detect', methods=['POST'])
def detect():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file found'}), 400
        
        image_file = request.files['image']
        image_array = np.frombuffer(image_file.read(), np.uint8)
        image_cv2 = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        
        # Perform object detection and face recognition
        results = detector.predict(image_cv2)
        
        # Process the results
        detected_objects = []
        recognized_faces = []
        for result in results:
            if 'faces' in result:
                for face_data in result['faces']:
                    # Extract face encoding
                    face_encoding = face_data.get('encoding')
                    if face_encoding:
                        # Recognize the face
                        name = recognize_face(face_encoding)
                        recognized_faces.append({'name': name})
            
            if 'objects' in result:
                for obj_data in result['objects']:
                    detected_objects.append({'type': obj_data.get('type')})
        
        # Send email if unknown faces detected
        if any(face.get('name') == 'Unknown' for face in recognized_faces):
            send_email('Unknown')
        
        return jsonify({'objects': detected_objects, 'faces': recognized_faces})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
