#!/usr/bin/node

function rec (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  } else {
    return a * rec(a - 1);
  }
}

console.log(rec(process.argv[2]));
