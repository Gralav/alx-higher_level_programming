#!/usr/bin/node
/* Function that return the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
