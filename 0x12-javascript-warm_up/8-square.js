#!/usr/bin/node
const myArgs = process.argv.slice(2);
let myStr = '';

if (isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(myArgs[0]); i++) {
    myStr += 'X';
  }
  for (let j = 0; j < parseInt(myArgs[0]); j++) {
    console.log(myStr);
  }
}
