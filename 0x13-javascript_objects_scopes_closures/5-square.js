#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Declaration
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
