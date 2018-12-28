#!/bin/python3
import sys

def solve(n):
    n1 = 0
    n2 = 2
    n3 = 8
    sum = n1 + n2
    while n3 <= n:
        sum += n3
        n1 = n2
        n2 = n3
        n3 = 4 * n2 + n1
    return sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
