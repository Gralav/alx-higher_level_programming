#!/usr/bin/node
/* Script that imports an array and computes a new array */
const list = require('./100-data').list;
const arrayMultiplied = list.map((val, index) => {
  return index * val;
});
console.log(list);
console.log(arrayMultiplied);
