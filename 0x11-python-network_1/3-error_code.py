#!/usr/bin/python3
"""
Error code
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            html = res.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
