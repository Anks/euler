#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
sys.path.append('../lib')
from digits import get_digits

"""
I’m trying a very brute force approach here. There probably is a way to this
algebraically, not numerically.
"""

def is_palindrome(number):
    """ Return true if the number is a palindrome.
    
    Start dividing the number by 10, 100, 1000, etc to get the digits
    from the right-hand side of the number.
    """

    digits = get_digits(number)

    palindrome = True
    for (k, v) in zip(digits, reversed(digits)):
        if k != v:
            palindrome = False
            break

    return palindrome
                 

if __name__ == '__main__':
    three_digit_numbers = xrange(100, 1000)
    combinations = ((i, j) for i in three_digit_numbers for j in three_digit_numbers)

    product_of_combinations = (combination[0] * combination[1] for combination in combinations)
    palindromes = (number for number in product_of_combinations if is_palindrome(number))
    print max(palindromes)
