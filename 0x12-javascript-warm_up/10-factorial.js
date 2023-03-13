#!/usr/bin/node
const myArgs = process.argv.slice(2);

function factorial (x) {
  if (x < 0) return;
  if (x === 0) return 1;
  return x * factorial(x - 1);
}

if (isNaN(myArgs[0])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(myArgs[0])));
}
