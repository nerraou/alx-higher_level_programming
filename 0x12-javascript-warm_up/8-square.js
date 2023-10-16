#!/usr/bin/node

const value = parseInt(process.argv[2]);
if (isNaN(value)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < value) {
    console.log('#'.repeat(value));
    i++;
  }
}
