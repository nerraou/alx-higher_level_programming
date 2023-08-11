#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """text indentation"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(":", ".")
    text = text.replace("?", ".")
    texts = text.split(".")
    for t in texts:
        print(t.strip(" "), end="\n\n")
