#!/usr/bin/node

const myArray = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(myArray[0], function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  fs.writeFile(myArray[1], body, (err, data) => {
    if (err) console.log(err);
  });
});
