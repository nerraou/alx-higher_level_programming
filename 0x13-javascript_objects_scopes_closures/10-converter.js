#!/usr/bin/node

// Declaration
module.exports.converter = function (base) {
  return function convert (value) {
    return value.toString(base);
  };
};
