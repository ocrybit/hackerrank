#!/bin/python3
import sys

def solve(n):
    def s(m):
        q = (n - 1) // m
        return q * m * (1 + q) // 2
    return s(3) + s(5) - s(15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
