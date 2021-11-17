#!/bin/bash
# takes a URL as an argument, sends a DELETE request to the URL, and displays the body of the response.
curl -sI DELETE "$1"
