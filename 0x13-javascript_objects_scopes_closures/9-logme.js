#!/usr/bin/node

let count = 0;

// Declaration
module.exports.logMe = function (item) {
  console.log(`${count}:`, item);
  count++;
};
