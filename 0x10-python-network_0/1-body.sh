#!/bin/bash
<<<<<<< HEAD
#displays size of the body of the response
curl -i "$1" | grep -i Content-Length | awk '{print $2}'
=======
# displays body of response to GET request
curl -sL "$1" -X GET
>>>>>>> 24649d0 (Task 1)
