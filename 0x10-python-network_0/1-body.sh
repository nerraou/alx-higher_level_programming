#!/bin/bash
#cURL to the end
if [ "$(curl -sI -o "/dev/null" -w "%{http_code}" "$1")" == '200' ]; then curl -s "$1"; fi
