#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_digits(number):
    """ Return the digits present in the number """
    digits = []
    divisor = 10
    while number * 10.0 / divisor > 0.1:
        remainder = number % divisor
        digits.append(int(remainder / (divisor / 10))) # Find the first digit of this number
        number = number - remainder # Round-up the number so that there is no extra remainder
        divisor = divisor * 10 # increase the divisor to get the next number

    return digits
