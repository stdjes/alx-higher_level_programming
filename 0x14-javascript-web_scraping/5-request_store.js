#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const filePath = process.argv[3];

request(apiUrl).pipe(fs.createWriteStream(filePath));
