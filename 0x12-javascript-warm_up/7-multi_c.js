#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  let index = 0;
  while (index < value) {
    console.log('C is fun');
    index++;
  }
}
