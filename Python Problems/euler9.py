# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Trying Euclid's formula for generating primitive Pythagorean triples
# a  = m^2 - N^2; b = 2*m*n; c = m^2 + n^2; m > n > 0

#To solve, we can set m^2 - n^2 + 2*m*n + m^2 + n^2 = 1000
# 2m^2 +2*m*n = 1000
# m(m + n) = 500

# m = 20; n = 5; a = 375; b = 200; c = 425
# a*b*c = 31875000

import math

