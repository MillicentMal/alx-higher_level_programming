#!/usr/bin/node
/*
script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
*/
let i = 0;
const Languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (i = 0; i < Languages.length; i++) {
  console.log(Languages[i]);
}
