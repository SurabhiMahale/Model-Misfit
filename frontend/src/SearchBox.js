
import React, { useState } from "react";

const SearchBox = ({ data }) => {
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  const handleInputChange = (event) => {
    const query = event.target.value;
    setSearchQuery(query);

    // Filter the data based on the search query
    const filteredResults = data.filter(item =>
      item.toLowerCase().includes(query.toLowerCase())
    );

    // Update the search results
    setSearchResults(filteredResults);
  };

  return (
    <div className="search_box">
      <input
        type="text"
        placeholder="Search EasyPay"
        value={searchQuery}
        onChange={handleInputChange}
      />
      <i className="fas fa-magnifying-glass"></i>
      {/* Display search results */}
      <ul>
        {searchResults.map((result, index) => (
          <li key={index}>{result}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchBox;
