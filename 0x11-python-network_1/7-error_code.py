#!/usr/bin/python3
"""
Response Error status
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    res = r.text
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(res)
