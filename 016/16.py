#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib')
from digits import get_digits

print sum(reversed(get_digits(2 ** 1000)))
