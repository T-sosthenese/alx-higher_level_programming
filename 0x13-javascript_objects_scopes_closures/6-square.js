#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let stringSquare = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        if (c) {
          stringSquare += c;
        } else {
          stringSquare += 'X';
        }
      }
      if (i < this.height) {
        stringSquare += '\n';
      }
    }
    console.log(stringSquare);
  }
}

module.exports = Square;
