#!/usr/bin/node
/*
script that prints the addition of 2 integers
*/

function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);

  if (isNaN(a, b)) {
    console.log('NaN');
  } else {
    const sum = a + b;
    console.log(sum);
  }
}
add();
