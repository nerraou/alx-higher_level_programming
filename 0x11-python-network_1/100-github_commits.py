#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/repos/rails/rails/commits?per_page=10'
    r = requests.get(url)
    commits = r.json()
    for commit in commits:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
