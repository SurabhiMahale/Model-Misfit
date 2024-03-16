import mongoose from 'mongoose';

const settingsSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User', // Reference to the User model
    required: true
  },
  fireAlert: {
    type: Boolean,
    default: false
  },
  intrusionAlert: {
    type: Boolean,
    default: false
  },
  violenceAlert: {
    type: Boolean,
    default: false
  },
  weaponAlert: {
    type: Boolean,
    default: false
  },
  theftAlert: {
    type: Boolean,
    default: false
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

export default mongoose.model('Settings', settingsSchema);
