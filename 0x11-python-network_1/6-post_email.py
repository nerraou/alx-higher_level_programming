#!/usr/bin/python3
"""
Response header value
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
