import express from 'express';
import Settings from '../models/settings.js';

const router = express.Router();

// POST route to create or update settings
router.post('/settings', async (req, res) => {
  try {
    const { userId, fireAlert, intrusionAlert, violenceAlert, weaponAlert, theftAlert } = req.body;

    // Check if settings exist for the user
    let settings = await Settings.findOne({ userId });

    // If settings don't exist, create new settings
    if (!settings) {
      settings = new Settings({
        userId,
        fireAlert,
        intrusionAlert,
        violenceAlert,
        weaponAlert,
        theftAlert
      });
    } else {
      // If settings exist, update them
      settings.fireAlert = fireAlert;
      settings.intrusionAlert = intrusionAlert;
      settings.violenceAlert = violenceAlert;
      settings.weaponAlert = weaponAlert;
      settings.theftAlert = theftAlert;
    }

    // Save or update settings
    await settings.save();

    res.status(200).send({ msg: 'Settings saved successfully' });
  } catch (error) {
    console.error('Error saving settings:', error);
    res.status(500).send({ msg: 'Internal server error' });
  }
});

// PUT route to update settings by user ID
router.put('/settings/:userId', async (req, res) => {
  try {
    const { userId } = req.params;
    const { fireAlert, intrusionAlert, violenceAlert, weaponAlert, theftAlert } = req.body;

    // Find settings by user ID
    const settings = await Settings.findOneAndUpdate(
      { userId },
      {
        fireAlert,
        intrusionAlert,
        violenceAlert,
        weaponAlert,
        theftAlert
      },
      { new: true }
    );

    if (!settings) {
      return res.status(404).send({ msg: 'Settings not found' });
    }

    res.status(200).send({ msg: 'Settings updated successfully', settings });
  } catch (error) {
    console.error('Error updating settings:', error);
    res.status(500).send({ msg: 'Internal server error' });
  }
});

export default router;
