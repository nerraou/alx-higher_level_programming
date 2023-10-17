#!/usr/bin/node
const SquareBase = require('./5-square');

// Declaration
module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
