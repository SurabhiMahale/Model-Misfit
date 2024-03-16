// CameraComponent.jsx
import React, { useRef, useEffect } from 'react';

const CameraComponent = () => {
  const videoRef = useRef(null);

  useEffect(() => {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
          videoRef.current.srcObject = stream;
        })
        .catch(function(error) {
          console.error('Error accessing camera:', error);
        });
    } else {
      console.error('getUserMedia not supported');
    }
  }, []);

  return (
    <div className="camera-component">
      <h2>Camera Feed</h2>
      <video ref={videoRef} width="100%" height="auto" autoPlay ></video>
    </div>
  );
};

export default CameraComponent;
