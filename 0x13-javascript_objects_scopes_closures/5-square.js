#!/usr/bin/node
// square inherits from the Rectangle class found in the 4-Rectangle.js file
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
