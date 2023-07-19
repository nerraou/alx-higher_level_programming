#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    key_max = list(a_dictionary.keys())[0]
    max = a_dictionary[key_max]
    for key in a_dictionary:
        if max < a_dictionary[key]:
            max = a_dictionary[key]
            key_max = key
    return max
