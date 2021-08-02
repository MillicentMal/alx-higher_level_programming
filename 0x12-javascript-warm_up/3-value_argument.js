#!/usr/bin/node
/*
script that prints the first argument passed to it:
*/

if (process.argv.length === 1) {
  console.log('No argument');
} else if (process.argv.length > 1) {
  console.log(process.argv[2]);
}
