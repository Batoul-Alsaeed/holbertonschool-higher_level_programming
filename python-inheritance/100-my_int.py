#!/usr/bin/python3
"""MyInt: A rebellious int that inverts equality operators"""


class MyInt(int):
    """Inverts == and != operators"""

    def __eq__(self, other):
        """Invert == to !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != to =="""
        return super().__eq__(other)
