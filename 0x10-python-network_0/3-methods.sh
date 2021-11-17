#!/bin/bash
#accepts URL as argument and displays body of response
curl -sX "$1" OPTIONS|grep "Allow"| cut -b 8- 
