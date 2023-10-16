#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const copy = process.argv.slice(2);
  const array = copy.map((x) => parseInt(x));
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
