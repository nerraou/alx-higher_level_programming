#!/bin/bash
# status code
curl -sL -o "/dev/null" -w "%{http_code}" "$1"
