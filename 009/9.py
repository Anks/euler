#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

numbers = range(1, 400) # a & b will be less than 400 each
combinations = ((a, b) for a in numbers for b in numbers)

a = b = c = None
found = False

for combination in combinations:
    a, b = combination

    ab_squared = a * a + b * b
    c = int(math.sqrt(ab_squared))

    if c * c == ab_squared and a + b + c == 1000:
        print a * b * c
        break
