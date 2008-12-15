#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib')
from primes import get_primes

primes = get_primes()
prime = None
for i in range(10001):
    prime = primes.next()
print prime
