#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

function requestCallback (error, _response, body) {
  if (error) {
    return console.log(error);
  }

  const parsedBody = JSON.parse(body);
  const usersStats = {};

  parsedBody.forEach((todo) => {
    if (todo.completed) {
      const currentCount = usersStats[todo.userId] || 0;

      usersStats[todo.userId] = currentCount + 1;
    }
  });

  console.log(usersStats);
}

request(url, requestCallback);
