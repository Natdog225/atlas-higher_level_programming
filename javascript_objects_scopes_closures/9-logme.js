#!/usr/bin/node

let count = 0; // Initialize a counter for the purpose of counting things.

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
