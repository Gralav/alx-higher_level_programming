#!/usr/bin/node
const myArgs = process.argv.slice(2);

function add (a, b) {
  return (a + b);
}

if (isNaN(myArgs[0]) || isNaN(myArgs[1])) {
  console.log('NaN');
} else {
  console.log(add(parseInt(myArgs[0]), parseInt(myArgs[1])));
}
