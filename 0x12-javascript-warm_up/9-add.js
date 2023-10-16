#!/usr/bin/node

const firstValue = parseInt(process.argv[2]);
const secondValue = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(firstValue, secondValue));
