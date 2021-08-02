#!/usr/bin/node
let largest = 0;
let larger = 0;
if (process.argv.length < 4) {
  console.log(0);
} 
else if (process.argv.length > 4 )
{
  for (let i = 0; i < process.argv.length; i++) {
     nums.push(process.argv[i]);
     }
     nums.sort(function(a,b) {return a-b});
  console.log(nums);
