#!/bin/bash
<<<<<<< HEAD
#displays size of the body of the response
curl -i "$1" | grep -i Content-Length | awk '{print $2}'
=======
# displays body of response to GET request
curl -sL "$1" -X GET
<<<<<<< HEAD
>>>>>>> 24649d0 (Task 1)
=======
<<<<<<< HEAD
>>>>>>> cb11bcb3feee63f84e504712a5a26bb09f9b0558
=======
>>>>>>> 24649d0 (Task 1)
>>>>>>> c604332 (Task 1)
>>>>>>> 9c6fe79 (Task 1)
