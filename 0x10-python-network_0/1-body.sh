#!/bin/bash
#cURL to the end
if [ "$(curl -sL -o "/dev/null" -w "%{http_code}" "$1")" == '200' ]; then curl -sL "$1"; fi
