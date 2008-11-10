#!/usr/bin/env python

# A created an infinite generator first, but then using it
# turned out to be a bit tricky. This code is much more readable.

def create_fibonacci_generator(max_value):
    """ Return a generator for fibonacci terms less than the input max value """
    a = 0
    b = 1
    yield a
    while b < max_value:
        a, b = b, a + b
        yield a
    
# Get numbers less than 4 million
terms = (term for term in create_fibonacci_generator(4000000))

# get the even terms
even_terms = (term for term in terms if term % 2 == 0)

print sum(even_terms)
