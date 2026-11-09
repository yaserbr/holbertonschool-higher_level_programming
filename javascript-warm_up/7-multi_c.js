#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  while (process.argv[2] > 0) {
    console.log('C is fun');
    process.argv[2]--;
  }
}
