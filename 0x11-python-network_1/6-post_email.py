#!/usr/bin/python3
"""
Post an email
"""


if __name__ == "__main__":
    import requests
    import sys
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    res = r.text
    print(res)
