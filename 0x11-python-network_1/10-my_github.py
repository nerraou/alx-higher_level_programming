#!/usr/bin/python3
"""
My Github
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    res = r.json()
    print(res.get("id"))
