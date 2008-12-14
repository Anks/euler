#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Another brute force solution, am too tired to think. There should be a
really simple formula to calculate something like this.
"""

def get_numbers():
    """
    The number in question should be divisible by the numbers 1-10 as
    well, of course.  They've helpfully provided a starting point, 2520,
    and any other numbers we consider will also be divisible by 1-10, so
    they'll be multiples of 2520.
    """
    start = 0
    while True:
        start = start + 2520
        yield start

def divisible_by_all(number, divisors):
    """ A little unpythonic, this """
    return all(map(lambda divisor: number % divisor == 0, divisors))

numbers = get_numbers()
current_number = numbers.next()

# I love how the next line. Python is really readable.
while not divisible_by_all(current_number, range(2, 21)):
    current_number = numbers.next()

print current_number
