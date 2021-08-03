#!/usr/bin/node

 let i = 0;

exports.logMe = function (item) {
// Output format: <number arguments already printed>: <current argument value>

  
  console.log(i + ':' + item);
  i++;
};
