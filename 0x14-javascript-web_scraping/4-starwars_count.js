#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const character = { id: 18, name: 'Wedge Antilles' };

request(apiUrl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    body = JSON.parse(body);
    let count = 0;
    for (const film of body.results) {
      const characters = film.characters;
      for (let i = 0; i < characters.length; i++) {
        if (characters[i].endsWith(character.id + '/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
