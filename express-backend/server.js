import express from "express";
import dotenv from "dotenv";
import connectDatabase from "./config/db.js";
import cors from "cors";
import userVerify from "./middlewares/userVerify.js";
import userRouter from "./controllers/userRouter.js";

dotenv.config();
const app = express();
connectDatabase();

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("Hello to fitness API");
});

app.get("/api", userVerify, (req, res) => {
    res.send({
      authenticated: true,
      user: req.user,
    });
  });
  
  app.use("/api/auth", userRouter);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server started at http://localhost:${PORT}`);
});