import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios';
import '../styles/alert_styles.css';

const AlertStack = () => {

    //#################### use after backned integration ####################
//   const [alerts, setAlerts] = useState([]);

//   useEffect(() => {
//     const fetchAlerts = async () => {
//       try {
//         const response = await axios.get('/api/alerts'); // Replace with your backend endpoint
//         setAlerts(response.data.alerts); // Assuming the response contains an array of alerts
//       } catch (error) {
//         console.error('Error fetching alerts:', error);
//       }
//     };

//     fetchAlerts();
//   }, []);

//   const removeAlert = (index) => {
//     setAlerts((prevAlerts) => prevAlerts.filter((_, i) => i !== index));
//   };
const [alerts, setAlerts] = useState([
    { id: 1, message: 'Alert 1', type: 'info' },
    { id: 2, message: 'Alert 2', type: 'warning' },
    { id: 3, message: 'Alert 3', type: 'error' },
  ]);

  const removeAlert = (id) => {
    setAlerts((prevAlerts) => prevAlerts.filter((alert) => alert.id !== id));
  };

  return (
    <Box className="box" sx={{ flexGrow: 1, maxWidth: 752 }}>
      <List className="alert-list"> {/* Add the class name */}
        {alerts.map((alert) => (
          <ListItem key={alert.id} className="alert-item"> {/* Add the class name */}
            <ListItemText primary={alert.message} />
            <IconButton edge="end" aria-label="delete" onClick={() => removeAlert(alert.id)}>
              <DeleteIcon className="delete-icon" /> {/* Add the class name */}
            </IconButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default AlertStack;
