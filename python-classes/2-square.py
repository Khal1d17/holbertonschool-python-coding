#!/usr/bin/python3
"""checkin size"""


class Square:
    """size"""
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    def __init__(self, size=0):
        self.__size = size
    def area(self):
        return self.__size**2
