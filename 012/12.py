#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def triangle_numbers():
    """ Return a generator for triangle numbers """
    current_sum = 0
    current_number = 0

    while True:
        current_number = current_number + 1
        current_sum = current_sum + current_number
        yield current_sum

def num_of_factors(number):
    """
    Returns the (approximate) number of factors for a number.

    I must confess, I cheated a bit to get this solution. I found out (thanks
    to Google) that for every divisor below the square root, there will be one
    above it as well. I don’t know why exactly, but it proved true when I did a
    test run with some random numbers.
    """

    num_factors = 1

    for current_number in range(2, int(math.sqrt(number))):
        if number % current_number == 0:
            num_factors = num_factors + 1

    return num_factors * 2

if __name__ == '__main__':
    numbers = triangle_numbers()
    number = numbers.next()

    while True:
        factor_length = num_of_factors(number)
        if factor_length > 500:
            print number
            break
        number = numbers.next()
