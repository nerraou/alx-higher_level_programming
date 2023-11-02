#!/bin/bash
# get allowed methods
curl -X OPTIONS -I -s "$1" | grep "Allow" | cut -c8-
