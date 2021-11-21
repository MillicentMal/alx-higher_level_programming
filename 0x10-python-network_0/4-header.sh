#!/bin/bash
#sends get request and displays body of response
curl   GET -sH "X-School-User-Id: 98" "$1"
