#!/usr/bin/node

const numOccurrences = parseInt(process.argv[2]);

if (isNaN(numOccurrences)) {
  console.log('Missing number of occurrences'); 
} else {
  let result = '';
  for (let i = 0; i < numOccurrences; i++) {
    result += 'C is fun\n'; 
  }
  console.log(result); 
}