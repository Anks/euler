#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib')
from primes import get_primes

def get_primes_less_than(number):
    primes = get_primes()

    while True:
        current_prime = primes.next()
        if current_prime > number:
            break
        else:
            yield current_prime

print sum(get_primes_less_than(2000000))
