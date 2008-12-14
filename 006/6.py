#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Behold the readability of the solution.
"""

def square(number):
    return number * number

def sum_of_squares(numbers):
    return sum(map(square, numbers))

def square_of_sum(numbers):
    return square(sum(numbers))

numbers = range(1, 101)
print square_of_sum(numbers) - sum_of_squares(numbers)
