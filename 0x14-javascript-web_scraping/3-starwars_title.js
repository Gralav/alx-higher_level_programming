#!/usr/bin/node
/*
 * Script that prints the title of a Star Wars movie where the episode number
 * matches a given integer.
*/

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');

request(url, function (err, result, body) {
  console.log(JSON.parse(body).title);
  if (err) {
    console.log(err);
  }
});
