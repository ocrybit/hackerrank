#!/bin/python3

import sys

def getFactors(n):
    factors = {}
    d = 2
    q = n
    lpf = 0
    while d ** 2 <= n:
        if q % d == 0:
            lpf = d
            q //= d
            if not d in factors: factors[d] = 0
            factors[d] += 1
            
        else:
            d += 1
    if not q in factors: factors[q] = 0
    factors[q] += 1    
    return factors

def solve(n):
    nums = {}
    for i in range(n, 0, -1):
        factors = getFactors(i)
        for key, val in factors.items():
            if not key in nums: nums[key] = 0
            nums[key] = max(nums[key], val)
    prod = 1
    for key, val in nums.items():
        prod *= (key ** val)
    return prod

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
