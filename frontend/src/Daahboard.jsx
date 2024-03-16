// Dashboard.jsx
import React, { useState } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBell, faChartLine, faCog } from "@fortawesome/free-solid-svg-icons";
import CameraComponent from "./Camera";
import Alert from '@mui/material/Alert';

import AlertTitle from '@mui/material/AlertTitle';

import SpeedometerComponent from "./SpeedometerComponent";
import "./style.css";

const Dashboard = () => {
  const data = [
    { name: "Dashboard", icon: faChartLine },
    { name: "Alerts", icon: faBell },
    { name: "Reports", icon: faChartLine },
    { name: "Settings", icon: faCog }
  ];

  const [searchQuery, setSearchQuery] = useState("");

  const handleInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <div>
      <div className="header">
        <div className="logo">
          <a href="#">Track</a>
          <div className="search_box">
            <input
              type="text"
              placeholder="Search EasyPay"
              value={searchQuery}
              onChange={handleInputChange}
            />
          </div>
        </div>
        <div className="header-icons">
          <FontAwesomeIcon icon={faBell} />
          <div className="account">
            <img src="data:image/jpeg;base64,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" alt="" />
            <h4>Jhon Viek</h4>
          </div>
        </div>
      </div>
      <div className="container">
        <nav>
          <div className="side_navbar">
            <span>Main Menu</span>
            {data.map((item, index) => (
              <a
                key={index}
                href="#"
                className={searchQuery && item.name.toLowerCase().includes(searchQuery.toLowerCase()) ? "menu-item-searched" : "menu-item"}
              >
                <div className="icon">
                  <FontAwesomeIcon icon={item.icon} />
                </div>
                <div className="text">
                  {item.name}
                </div>
              </a>
            ))}
          </div>
        </nav>
        <div className='content'>
          <div className='Main_component'>
            <div className='camera_component'>
              <h2>Camera Feed</h2>
              <CameraComponent/>
            </div>
            <div className='speedometer_component'>
              <h2>Speedometer</h2>
              <SpeedometerComponent/>
            </div>
          </div>
        </div>
        <div className="sidebar">
          <h4>Account Balance</h4>
          <div className="error_1">
            <Alert severity="error">
  <AlertTitle>Error</AlertTitle>
  This is an error Alert with a scary title.
</Alert>
</div>


<div>
  <Alert severity="error">
  <AlertTitle>Error</AlertTitle>
  This is an error Alert with a scary title.
</Alert>
</div>



       </div>
      </div>
    </div>
  );
};

export default Dashboard;
