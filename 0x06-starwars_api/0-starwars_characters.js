#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmID) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmID;

  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const charcaters = response.characters;

  for (let i = 0; i < charcaters.length; i++) {
    const urlCharacter = charcaters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(filmID);
