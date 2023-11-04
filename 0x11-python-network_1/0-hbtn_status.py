#!/usr/bin/python3
"""
fetch from url use urllibe
"""


if __name__ == "__main__":
    import urllib.request

    def try_utf8(data):
        "Returns a Unicode object on success, or None on failure"
        try:
            return data.decode('utf-8')
        except UnicodeDecodeError:
            return None
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        html = res.read()
        udata = try_utf8(html)
        if udata is None:
            check_utf8 = ""
        else:
            check_utf8 = "OK"
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(check_utf8))
