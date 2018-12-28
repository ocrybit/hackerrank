#!/bin/python3
import sys

def solve(n):
    d = 2
    q = n
    lpf = 0
    while d ** 2 <= n:
        if q % d == 0:
            lpf = d
            q //= d
        else:
            d += 1
    return max(q,lpf)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
