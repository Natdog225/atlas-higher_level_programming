#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    const result = n * factorial(n - 1);
    console.log(result);
    return result;
  }
}

const num = parseInt(process.argv[2]);
factorial(num);