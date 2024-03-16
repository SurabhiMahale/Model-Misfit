import React, { useState, useRef } from "react";
import {
  TextField,
  Button,
  Container,
  Snackbar,
  Alert,
  Grid,
  CardMedia,
  Typography,
} from "@mui/material";
import yourImage from "./assets/signin.svg";
import axios from "axios";
import { Link } from "react-router-dom";
import "./Login.css"; // Import CSS file

const Login = () => {
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [severity, setSeverity] = useState("error");
  const emailRef = useRef(null);
  const passwordRef = useRef(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const email = emailRef.current.value;
      const password = passwordRef.current.value;

      const response = await axios.post(
        `${process.env.REACT_APP_BACKEND_URI}/api/auth/login`,
        { email, password }
      );

      if (response.data.token) {
        localStorage.setItem("token", response.data.token);
        setMessage(response.data.msg);
        setSeverity("success");
        setOpen(true);
        setTimeout(() => {
          window.location.href = "/"; // Redirect to home page
        }, 1000);
      }
    } catch (error) {
      setMessage(error.response.data.msg);
      setOpen(true);
    }
  };

  return (
    <Container maxWidth={false} className="container">
      <Grid className="card">
        <Grid item xs={6}>
          <CardMedia
            component="img"
            image={yourImage}
            alt="trainer"
            className="image"
          />
        </Grid>
        <Grid item xs={6}>
          <Grid className="form">
            <form onSubmit={handleSubmit}>
              <Typography variant="h5" align="center" gutterBottom className="form-title">
                Login
              </Typography>
              <TextField
                inputRef={emailRef}
                label="Email"
                type="email"
                variant="outlined"
                fullWidth
                required
                margin="normal"
                className="input"
              />
              <TextField
                inputRef={passwordRef}
                label="Password"
                type="password"
                variant="outlined"
                fullWidth
                required
                margin="normal"
                className="input"
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                className="button"
              >
                Login
              </Button>
              <Link to="/signup" className="link">
                <Button
                  variant="outlined"
                  color="primary"
                  fullWidth
                  className="button"
                >
                  Register
                </Button>
              </Link>
            </form>
            <Snackbar
              open={open}
              autoHideDuration={6000}
              onClose={() => setOpen(false)}
              anchorOrigin={{ vertical: "top", horizontal: "right" }}
              className="snackbar"
            >
              <Alert severity={severity} variant="outlined" className="alert">
                {message}
              </Alert>
            </Snackbar>
          </Grid>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Login;
