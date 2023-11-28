#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  const responseBody = JSON.parse(body);
  if (error) console.error('error:', error);
  let count = 0;
  responseBody.results.forEach((element) => {
    for (let index = 0; index < element.characters.length; index++) {
      const position = element.characters[index].search(/18/);
      if (position !== -1) count++;
    }
  });
  console.log(count);
});
