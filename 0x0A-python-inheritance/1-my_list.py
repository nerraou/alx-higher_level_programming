#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """
    MYlist class inherate from list class
    """
    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))
