#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
