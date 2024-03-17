import React, { useState } from "react";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";
import Button from "@mui/material/Button";
import axios from "axios";
import "../styles/settings.css";

const Settings = ({ handleSettingsChange }) => {
  const [settings, setSettings] = useState({
    fireAlert: false,
    intrusionAlert: false,
    violenceAlert: false,
    weaponAlert: false,
    theftAlert: false,
  });

  const handleToggle = (event) => {
    const { name, checked } = event.target;
    setSettings({ ...settings, [name]: checked });
  };

  const saveSettings = async () => {
    try {
      const response = await axios.post("/api/settings", settings);

      if (response.status === 200) {
        console.log("Settings saved successfully");
        // Pass the updated settings to the parent component
        handleSettingsChange(settings);
      } else {
        console.error("Failed to save settings");
      }
    } catch (error) {
      console.error("Error saving settings:", error);
    }
  };

  return (
    <div className="settings_body">
      <div className="settings-container">
        <h3>Alert Settings</h3>
        <FormControlLabel
          control={
            <Switch
              checked={settings.fireAlert}
              onChange={handleToggle}
              name="fireAlert"
            />
          }
          label="Fire Alert"
        />
        <FormControlLabel
          control={
            <Switch
              checked={settings.intrusionAlert}
              onChange={handleToggle}
              name="intrusionAlert"
            />
          }
          label="Intrusion Alert"
        />
        <FormControlLabel
          control={
            <Switch
              checked={settings.violenceAlert}
              onChange={handleToggle}
              name="violenceAlert"
            />
          }
          label="Violence Alert"
        />
        <FormControlLabel
          control={
            <Switch
              checked={settings.weaponAlert}
              onChange={handleToggle}
              name="weaponAlert"
            />
          }
          label="Weapon Alert"
        />
        <FormControlLabel
          control={
            <Switch
              checked={settings.theftAlert}
              onChange={handleToggle}
              name="theftAlert"
            />
          }
          label="Theft Alert"
        />
      </div>
      <Button
        className="button_settings"
        variant="outlined"
        color="primary"
        onClick={saveSettings}
      >
        Save Settings
      </Button>
    </div>
  );
};

export default Settings;
