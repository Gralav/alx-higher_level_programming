#!/usr/bin/node
/*
 * Script that prints the number of movies where the character "Wedge Antilles"
 * is present.
*/
const url = process.argv[2];
const request = require('request');

request(url, function (err, result, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      const tempCount = films[i].characters.toString().match(/18/g);
      if (tempCount !== null) {
        count = count + tempCount.length;
      }
    }
    console.log(count);
  }
});
