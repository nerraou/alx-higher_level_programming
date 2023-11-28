#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  const responseBody = JSON.parse(body);

  if (error) {
    console.error('error:', error);
  }
  responseBody.characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      const responseBody = JSON.parse(body);
      console.log(responseBody.name);
    });
  });
});
