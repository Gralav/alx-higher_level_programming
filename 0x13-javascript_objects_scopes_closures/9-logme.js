#!/usr/bin/node
/* Function that prints the number of arguments already printed and the new
 * argument value */
let index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`);
  index = index + 1;
};
