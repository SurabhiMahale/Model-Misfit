// Update the WebcamComponent.jsx file

import React, { useState, useEffect, useRef } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

const WebcamComponent = () => {
  const [frame, setFrame] = useState(null);
  const [annotations, setAnnotations] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const videoStream = await fetch('http://127.0.0.1:5001/video_feed');
      const annotationsData = await fetch('/annotations');

      // Process annotations
      const annotationsJson = await annotationsData.json();
      setAnnotations(annotationsJson);

      // Process video stream
      const videoBlob = await videoStream.blob();
      const videoUrl = URL.createObjectURL(videoBlob);
      setFrame(videoUrl);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Object Detection</h1>
      {frame && <img src={frame} alt="Video Stream" />}
      <ul>
        {annotations.map((annotation, index) => (
          <li key={index}>{annotation}</li>
        ))}
      </ul>

    </div>
  );
};

export default WebcamComponent;
