#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 18; // Character ID for Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body);
      let count = 0;

      // Iterate through each film in the results
      filmsData.results.forEach(film => {
        if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)) {
          count++;
        }
      });

      console.log(count);

    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
