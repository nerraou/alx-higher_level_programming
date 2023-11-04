#!/usr/bin/python3
"""
Post an email
"""


if __name__ == "__main__":
    import requests
    import sys
    value = ""
    if len(sys.argv) == 2:
        value = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': value})
    try:
        res = r.json()
        if len(res) > 0:
            print("[{}] {}".format(res["id"], res["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
