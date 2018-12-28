#!/bin/python3
import sys

def sum(n,m):
    q = (n - 1) // m
    l = m * q
    return (q * (m + l)) // 2

def solve(n): return sum(n, 3) + sum(n, 5) - sum(n, 15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
