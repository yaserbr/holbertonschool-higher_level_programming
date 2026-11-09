#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  let str = '';
  for (let index = 0; index < process.argv[2]; index++) {
    str = '';
    for (let index = 0; index < process.argv[2]; index++) {
      str += 'x';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
