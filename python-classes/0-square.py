#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

my_square = Square(3)

print(my_square.area())

try:
    print(my_square.__size)
except AttributeError as e:
    print(e)

print(my_square._Square__size)
