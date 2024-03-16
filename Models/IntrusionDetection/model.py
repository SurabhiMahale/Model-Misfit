import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models, utils

# Function to load and preprocess image data
def load_data(data_dir):
    images = []
    labels = []
    label_dict = {'authorized': 0, 'unauthorized': 1}  # Map labels to numeric values
    
    for label in label_dict.keys():
        label_path = os.path.join(data_dir, label)
        for filename in os.listdir(label_path):
            if filename.endswith(".jpg"):
                img_path = os.path.join(label_path, filename)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (100, 100))  # Resize image to a fixed size
                images.append(img)
                labels.append(label_dict[label])
    
    return np.array(images), np.array(labels)

# Load and preprocess data
# Load and preprocess data
data_dir = "images"  # Update the directory path
images, labels = load_data(data_dir)


# Split data into training and testing sets
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

# Normalize pixel values to range [0, 1]
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# Define CNN architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# Save the model
model.save('facial_recognition_model.h5')
