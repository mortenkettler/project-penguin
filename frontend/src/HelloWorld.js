import React, { useState } from 'react';

function HelloWorld() {
  const [message, setMessage] = useState(''); // State to store the message from the backend

  // Function to fetch the message from the backend
  const fetchMessage = async () => {
    try {
      const response = await fetch('http://localhost:5000/hello'); // Flask backend URL
      const data = await response.json(); // Parse JSON response
      setMessage(data.message); // Set the message in state
    } catch (error) {
      console.error("Error fetching message:", error);
      setMessage("Error fetching message"); // Set an error message in state if request fails
    }
  };

  return (
    <div>
      <h1>{message || "Click the button to fetch the message!"}</h1>
      <button onClick={fetchMessage}>Get "Hello, World!" Message</button>
    </div>
  );
}

export default HelloWorld;
