#!/usr/bin/node
const request = require('request');

// Get the URL to request from the command line
const url = process.argv[2];

// Make a GET request to the URL
request(url, (error, response) => {
  if (error) {
    // If an error occurs during the request, print the error object
    console.error(error);
  } else {
    // If the request is successful,print code.
    console.log('code:', response.statusCode);
  }
});
