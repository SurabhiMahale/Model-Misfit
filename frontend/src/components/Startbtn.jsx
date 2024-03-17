import React from 'react';
import axios from 'axios';

class Startbtn extends React.Component {
  handleClick = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5001/generate-csv', {}, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log('CSV file generated successfully');
    } catch (error) {
      console.error('Error generating CSV file:', error.message);
    }
  };

  render() {
    return (
      <button onClick={this.handleClick}>
        Generate CSV
      </button>
    );
  }
}

export default Startbtn;
