// Update the WebcamComponent.jsx file

import React, { useState, useEffect, useRef } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

const WebcamComponent = () => {
  const webcamRef = useRef(null);
  const [results, setResults] = useState([]);
  const intervalRef = useRef(null);

  const sendFrameToServer = async () => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      const blob = await fetch(imageSrc).then(res => res.blob());
      const formData = new FormData();
      formData.append('image', blob, 'frame.jpeg');
      try {
        const response = await axios.post('http://localhost:5001/detect', formData);
        setResults(response.data);
      } catch (error) {
        console.error('Error processing frame:', error);
      }
    }
  };

  useEffect(() => {
    // Start sending frames at the specified interval
    intervalRef.current = setInterval(() => {
      sendFrameToServer();
    }, 500); // Send frame every 500 milliseconds

    // Stop sending frames when the component unmounts
    return () => clearInterval(intervalRef.current);
  }, []);

  return (
    <div>
      <Webcam
        ref={webcamRef}
        screenshotFormat="image/jpeg"
      />
      {/* Display results */}
      <div>
        {results && results.objects && results.objects.map((obj, index) => (
          <div key={index}>
            <p>Type: {obj.type}</p>
          </div>
        ))}
        {results && results.faces && results.faces.map((face, index) => (
          <div key={index}>
            <p>Name: {face.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WebcamComponent;
