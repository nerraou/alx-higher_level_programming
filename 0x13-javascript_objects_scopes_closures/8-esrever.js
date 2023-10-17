#!/usr/bin/node

// Declaration
module.exports.esrever = function (list) {
  const reversed = [];

  for (let i = list.length - 1; i >= 0; i--) {
    const element = list[i];
    reversed.push(element);
  }

  return reversed;
};
