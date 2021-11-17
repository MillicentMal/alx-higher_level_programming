#!/bin/bash
# Takes in a URL as an argument, sends a POST request, with a body displays the body of the response.
curl -s -d "email:test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
