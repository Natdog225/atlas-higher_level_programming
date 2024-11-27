#!/usr/bin/node
// Include the request module for making HTTP requests
const request = require('request');

// Get the movie ID
const movieId = process.argv[2];

// Construct the API URL with the movie ID
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else {
    // If the request is successful, parse and print the title
    try {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError); 1 
    }
  }
});
