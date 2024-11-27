#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file 
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurs, print the error object
    console.error(err);
  } else {
    // If the read is successful, print dat thang
    console.log(data);
  }
});