#!/usr/bin/node
/* Write a class Rectangle that defines a square and inherist from Rectangle of
 * 4-rectangle.js */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
