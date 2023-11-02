#!/bin/bash
# post request
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
