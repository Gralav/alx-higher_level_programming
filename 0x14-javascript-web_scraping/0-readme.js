#!/usr/bin/node

const fs = require('fs');

const myArray = process.argv.slice(2);

fs.readFile(myArray[0], 'utf-8', (err, data) => {
  if (err) { console.log(err); } else { process.stdout.write(data); }
});
