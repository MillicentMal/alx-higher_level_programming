#!/bin/bash
<<<<<<< HEAD
#displays size of the body of the response
curl -i "$1" | grep -i Content-Length | awk '{print $2}'
=======
# displays body of response to GET request
curl -sL "$1" -X GET
>>>>>>> cb11bcb3feee63f84e504712a5a26bb09f9b0558
