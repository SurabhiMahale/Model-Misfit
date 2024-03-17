import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import '../styles/alert_styles.css';

const Alert = ({ settings }) => {
    const [alerts, setAlerts] = useState([]);
    const [snackbarOpen, setSnackbarOpen] = useState(false);
    const [snackbarMessages, setSnackbarMessages] = useState([]);

    useEffect(() => {
        const knownUserTimer = setInterval(() => {
            if (settings.fireAlert) createAlert('Fire Alert', 'error');
            if (settings.intrusionAlert) createAlert('Intrusion Alert', 'warning');
            if (settings.violenceAlert) createAlert('Violence Alert', 'error');
            if (settings.weaponAlert) createAlert('Weapon Alert', 'error');
            if (settings.theftAlert) createAlert('Theft Alert', 'warning');
        }, 5000);

        return () => {
            clearInterval(knownUserTimer);
        };
    }, [settings]);

    const createAlert = (message, type) => {
        const newAlert = { id: Date.now(), message, type };
        setAlerts((prevAlerts) => [...prevAlerts, newAlert]);
        setSnackbarMessages((prevMessages) => [...prevMessages, message]);
        setSnackbarOpen(true);
        setTimeout(() => {
            removeAlert(newAlert.id);
            setSnackbarOpen(false);
        }, 6000);
    };

    const removeAlert = (id) => {
        setAlerts((prevAlerts) => prevAlerts.filter((alert) => alert.id !== id));
    };

    const handleSnackbarClose = () => {
        setSnackbarOpen(false);
    };

    return (
        <Box className="box" sx={{ flexGrow: 1, maxWidth: 752 }}>
            <List className="alert-list">
                {alerts.map((alert) => (
                    <ListItem key={alert.id} className="alert-item">
                        <ListItemText primary={alert.message} />
                        <IconButton edge="end" aria-label="delete" onClick={() => removeAlert(alert.id)}>
                            <DeleteIcon className="delete-icon" />
                        </IconButton>
                    </ListItem>
                ))}
            </List>
            <Snackbar
                anchorOrigin={{ vertical: 'bottom', horizontal: 'left' }}
                open={snackbarOpen}
                autoHideDuration={6000}
                onClose={handleSnackbarClose}
            >
                <MuiAlert onClose={handleSnackbarClose} severity="info" sx={{ width: '100%' }}>
                    {snackbarMessages.join('\n')}
                </MuiAlert>
            </Snackbar>
        </Box>
    );
};

export default Alert;
