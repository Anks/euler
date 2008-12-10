#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
            if prime > (num / 2):
                return True
    
    _primes = [2] # Holds all prime numbers found so far


    yield _primes[0]

    num = _primes[0] + 1 

    while True:
        if is_prime(num, _primes):
            _primes.append(num)
            yield num

	num = num + 2 # We’re interested in odd numbers only

primes = get_primes()
prime = None
for i in range(10001):
    prime = primes.next()
print prime
