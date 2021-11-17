#!/bin/bash
#accepts URL as argument and displays body of response
curl -sI  -X OPTIONS "$1"|grep "Allow"| cut -b 8- 
