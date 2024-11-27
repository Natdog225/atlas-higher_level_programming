#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach(todo => {
        if (todo.completed) {
          const userId = todo.userId;
          if (completedTasksByUser[userId]) {
            completedTasksByUser[userId]++;
          } else {
            completedTasksByUser[userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);

    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
