#!/usr/bin/node

// Declaration
module.exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const item of list) {
    if (item === searchElement) {
      count++;
    }
  }
  return count;
};
