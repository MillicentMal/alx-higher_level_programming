#!/bin/bash
#sends get request and displays body of response
curl -sI -X GET "$1" -H "X-School-User-Id: 98"
