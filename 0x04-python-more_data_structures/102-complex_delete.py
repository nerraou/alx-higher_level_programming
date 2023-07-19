#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    keys_to_delete = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        a_dictionary.pop(key)
    return a_dictionary
