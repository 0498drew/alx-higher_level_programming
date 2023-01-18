#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error}`);
    return;
  }
  const film = JSON.parse(body);
  for (const character of film.characters) {
    request.get(character, (error, response, body) => {
      if (error) {
        console.log(`Error: ${error}`);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
