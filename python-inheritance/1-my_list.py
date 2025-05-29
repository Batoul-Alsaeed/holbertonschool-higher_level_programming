#!/usr/bin/python3
"""
MyList module that inherits from built-in list
"""


class MyList(list):
    """
    Custom list class with additional method to print sorted list
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        """
        print(sorted(self))
