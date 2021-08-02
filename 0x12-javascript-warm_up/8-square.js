#!/usr/bin/node
/*
script that prints x times “C is fun”
*/
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('x');
  }
}
