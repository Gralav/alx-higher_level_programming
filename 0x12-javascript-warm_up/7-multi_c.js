#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (isNaN(myArgs[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(myArgs[0]); i++) {
    console.log('C is fun');
  }
}
