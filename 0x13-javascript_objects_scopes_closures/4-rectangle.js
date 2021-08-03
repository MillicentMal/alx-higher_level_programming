#!/sr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  double () {
    const width = 2 * this.width;
    const height = 2 * this.height;
    this.width = width;
    this.height = height;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};
