#!/bin/bash
#displays size of the body of the response
curl -i "$1" | grep -i Content-Length | awk '{print $2}'
