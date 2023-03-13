#!/usr/bin/node
const myArgs = process.argv.slice(2);

function secondMax (a) {
  if (a.length === 0 || a.length === 1) {
    console.log(0);
  } else {
    const varPop = Math.max(...a);
    const aCopy = [];
    for (let i = 0; i < a.length; i++) {
      if (parseInt(a[i]) !== varPop) {
        aCopy.push(a[i]);
      }
    }
    console.log(Math.max(...aCopy));
  }
}

secondMax(myArgs);
