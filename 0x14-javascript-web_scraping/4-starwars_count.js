#!/usr/bin/node
/*
 * Script that computes the number of tasks completed by user ID
 *
*/
const url = process.argv[2];
const request = require('request');
const tasksDict = {};

request(url, function (err, result, body) {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);

    for (let i = 0; i < tasks.length; i++) {
      if (!tasks[i].completed) {
        continue;
      }
      const userId = tasks[i].userId;
      if (userId in tasksDict) {
        tasksDict[userId] += 1;
        continue;
      }
      tasksDict[userId] = 1;
    }
  }
  console.log(tasksDict);
});
