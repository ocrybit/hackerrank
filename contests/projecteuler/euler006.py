#!/bin/python3
import sys

def solve(n):
    sum_square = (((1 + n) * n) // 2) ** 2
    square_sum = (n * (n + 1) * ((2 * n) + 1)) // 6
    return sum_square - square_sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
