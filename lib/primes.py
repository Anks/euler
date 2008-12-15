#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

"""
I’m generating an infinite series of prime numbers using
a method I remember from the SICP lectures. Fun.
"""

def get_primes():
    "Returns a generator that keeps outputting prime numbers"

    def is_prime(num, _primes):
        "Check if a number is prime, use the primes found so far "
        for prime in _primes:
            if num % prime == 0:
                return False
            if prime > math.sqrt(num):
                return True
    
    _primes = [2, 3, 5] # Holds all prime numbers found so far

    yield _primes[0]
    yield _primes[1]
    yield _primes[2]

    num = _primes[2] + 2

    while True:
        
        if is_prime(num, _primes):
            _primes.append(num)
            yield num

	num = num + 4 # All primes greater than 3 can be written in the form 6k+/-1.

        if is_prime(num, _primes):
            _primes.append(num)
            yield num

        num = num + 2
