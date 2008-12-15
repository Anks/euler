#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
sys.path.append('../lib')
from primes import get_primes
        
def prime_factors(number):
    " Return a generator with all the prime factors of the input number "
    primes = get_primes()
    current_prime = primes.next()

    while current_prime < math.sqrt(number):
        if number % current_prime == 0:
            yield current_prime
            
        current_prime = primes.next()

    raise StopIteration

print max(prime_factors(600851475143))
