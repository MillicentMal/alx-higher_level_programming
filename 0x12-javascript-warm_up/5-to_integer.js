#!/usr/bin/node
/*
script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
*/
const strtoint = parseInt(process.argv[2]);
if (isNaN(strtoint)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + strtoint);
}
