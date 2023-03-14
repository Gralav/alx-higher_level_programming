#!/usr/bin/node

const fs = require('fs');

const myArray = process.argv.slice(2);

fs.readFile(myArray[0], (err, data) => {
  if (err) throw err;
  fs.appendFile(myArray[2], data, (err) => {
    if (err) throw err;
  });
});
fs.readFile(myArray[1], (err, data) => {
  if (err) throw err;
  fs.appendFile(myArray[2], data, (err) => {
    if (err) throw err;
  });
});
