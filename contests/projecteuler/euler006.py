#!/bin/python3
import sys

def solve(n):
    sum1 = (((1 + n) * n) // 2) ** 2
    sum2 = (n * (n + 1) * ((2 * n) + 1)) // 6
    return abs(sum1 - sum2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
