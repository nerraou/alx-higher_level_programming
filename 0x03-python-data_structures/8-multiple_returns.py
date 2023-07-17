#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    new_tuple = ()
    length = len(sentence)
    if length == 0:
        new_tuple = (0, None)
    else:
        new_tuple = (length, sentence[0])
    return new_tuple
