#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringRectangle = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        stringRectangle += 'X';
      }
      if (i < this.height) {
        stringRectangle += '\n';
      }
    }
    console.log(stringRectangle);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
