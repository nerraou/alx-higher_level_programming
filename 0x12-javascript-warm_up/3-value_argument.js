#!/usr/bin/node

let lastIndex = 0;

process.argv.forEach((element, index) => {
  if (index > 1) {
    console.log(element);
  }
  lastIndex = index;
});
if (lastIndex <= 1) {
  console.log('No argument');
}
