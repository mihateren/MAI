from math import gcd
from sys import stdin

for x in stdin:
    print(gcd(*map(int, x.split())))