import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import validator from "validator"; 
import User from "../models/user.js";

const router = express.Router();

router.post("/register", async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // Validate email format
    if (!validator.isEmail(email)) {
      return res.status(400).send({ msg: "Invalid email format" });
    }

    // Validate password length
    if (!validator.isLength(password, { min: 6 })) {
      return res.status(400).send({ msg: "Password must be at least 6 characters long" });
    }
    const emailExists = await User.findOne({ email });

    if (emailExists) {
      return res.status(400).send({ msg: "Email already exists!" });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({
      name,
      email,
      password: hashedPassword,
    });

    await newUser.save();
    res.status(200).send({ msg: "User created Successfully!" });
  } catch (error) {
    res.status(500).send({ msg: error.message });
  }
});

router.post("/login", async (req, res) => {
  try {
    const { email, password } = req.body;

    const existingUser = await User.findOne({ email });
    if (!existingUser) {
      return res.status(400).send({ msg: "Email doesn't exist!" });
    }

    const isPasswordCorrect = await bcrypt.compare(password, existingUser.password);
    if (!isPasswordCorrect) {
      return res.status(400).send({ msg: "Password Incorrect!" });
    }

    console.log("JWT Secret:", process.env.JWT_SECRET );
    const token = jwt.sign({ _id: existingUser._id }, process.env.JWT_SECRET);
    res.status(200).send({ msg: "Login successful!", token });
  } catch (error) {
    res.status(500).send({ msg: error.message });
  }
});

// Define the DELETE route for deleting a user by ID
    router.delete("/delete", async (req, res) => {
      try {
        const { id } = req.query;
    
        const result = await User.deleteOne({ _id: id });
        if (result.deletedCount > 0) {
          res.status(200).send({ msg: "User data deleted successfully!" });
        } else {
          res.status(404).send({ msg: "User data not found or already deleted!" });
        }
      } catch (error) {
        console.log("Error:", error);
        res.status(500).send({ msg: "Internal server error" });
      }
    });


export default router;
