#!/usr/bin/python3
"""
Response header value
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        info = res.info()
        print(info["X-Request-Id"])
