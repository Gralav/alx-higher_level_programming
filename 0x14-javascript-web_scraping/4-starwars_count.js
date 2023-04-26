#!/usr/bin/node

const myArray = process.argv.slice(2);
const request = require('request');

request(myArray[0], function (error, response, body) {
  if (error) { console.log(error); } else {
    const results = JSON.parse(body).results;
    let count = 0;
    if (results && results.length >= 1) {
      results.forEach(dict => { if (dict.characters.includes('https://swapi.co/api/people/18/')) { count++; } });
    }
    console.log(count);
  }
});
