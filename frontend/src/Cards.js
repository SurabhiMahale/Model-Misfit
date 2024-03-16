import React from "react";
import "./CardsStyle.css"; // Import CSS file for styling

const Cards = () => {
  return (
    <div className="cards-container">
      <div className="card">
        <div className="card-content">Card 1</div>
      </div>
      <div className="card">
        <div className="card-content">Card 2</div>
      </div>
      <div className="card">
        <div className="card-content">Card 3</div>
      </div>
      <div className="card">
        <div className="card-content">Card 4</div>
      </div>
    </div>
  );
};

export default Cards;
