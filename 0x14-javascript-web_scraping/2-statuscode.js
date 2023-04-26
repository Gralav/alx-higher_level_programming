#!/usr/bin/node

const myArray = process.argv.slice(2);
const request = require('request');

request(myArray[0], function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  console.log('code:', response && response.statusCode);
});
