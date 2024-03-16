import jwt from "jsonwebtoken";
import User from "../models/user.js";

const userVerify = async (req, res, next) => {
  const token = req.header("auth-token");
  if (!token) {
    return res.status(401).send({
      msg: "Token not found!",
    });
  }

  try {
    let user = jwt.verify(token, process.env.JWT_SECRET);
    user = await User.findOne({ _id: user._id }, { name: 1 });
    req.user = user;
    next();
  } catch (error) {
    res.status(400).send({
      msg: error.message,
    });
  }
};

export default userVerify;