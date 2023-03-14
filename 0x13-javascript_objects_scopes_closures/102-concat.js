#!/usr/bin/node
const fs = require('fs');
let first = "";
let second = "";
fs.readFile('hola', 'utf-8', (err, data) =>{
  if (err) throw err;
  first = data;
  second = first + first + first;
  console.log(second);
});
