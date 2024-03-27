#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
