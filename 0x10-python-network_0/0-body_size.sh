#!/bin/bash
#get body size using curl
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
