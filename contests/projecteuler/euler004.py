#!/bin/python3

import sys

def solve(n):
    for i in range(n // 1000, 100, -1):
        num = int(str(i) + str(i)[::-1])
        if num < n:
            for i2 in range(100,1000):
                if num % i2 == 0:
                    q = num // i2
                    if q >= 100 and q < 1000:
                        return num

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
