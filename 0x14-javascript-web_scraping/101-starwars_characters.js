#!/usr/bin/node
/*
 * Script that prints all characters of a Star Wars Movie
 *
*/
const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    let i = 0;
    while(i < characters.length) {
      request.get(characters[i], (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
     i++;
    }
  }
});
