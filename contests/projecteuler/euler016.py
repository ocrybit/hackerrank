#!/bin/python3
import sys

def solve(n): return sum([int(n2) for n2 in str(2 ** n)])

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))



