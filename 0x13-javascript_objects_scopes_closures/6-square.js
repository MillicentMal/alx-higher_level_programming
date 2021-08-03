#!/usr/bin/node
// square inherits from the Rectangle class found in the 4-Rectangle.js file
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
}

charPrint(c)  {
if (c === undefined) {
c = 'X';
}
  
for (let i = 0; i < this.height; i++) {
for (let j = 0; j < this.width; j++) {
process.stdout.write(c);
}
process.stdout.write('\n');
}
}
};
