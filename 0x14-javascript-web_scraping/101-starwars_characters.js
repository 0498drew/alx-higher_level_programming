#!/usr/bin/node

const request = require("request");

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error}`);
    return;
  }
  const data = JSON.parse(body);
  const charactersList = data.characters;
  let promises = charactersList.map(character => {
    return new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });
  Promise.all(promises).then((values) => {
    values.forEach(character => {
      console.log(character);
    });
  }).catch((error) => {
    console.log(error);
  });
});
