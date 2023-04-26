#!/usr/bin/node

const fs = require('fs');

const myArray = process.argv.slice(2);

fs.writeFile(myArray[0], myArray[1], (err, data) => {
  if (err) console.log(err);
});
