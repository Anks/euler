#!/usr/bin/env python

def divisible_by(num, divisor):
    return num % divisor == 0

multiples = (n for n in xrange(1000)
             if divisible_by(n, 3) or divisible_by(n, 5))

print sum(multiples)
