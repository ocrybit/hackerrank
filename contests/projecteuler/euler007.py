#!/bin/python3
import sys

def getPrimes(n):
    nums = [None] * (n + 1)
    nums[0] = False
    nums[1] = False
    i = 2
    while i <= n:
        if nums[i] != False:
            nums[i] = True
            prod = i * 2
            while prod <= n:
                nums[prod] = False
                prod += i
        i += 1
    primes = []
    i3 = 0
    for v in nums:
        if v:
            primes.append(i3)
        i3 += 1
    return primes
primes = getPrimes(104750)

def solve(n):
    return primes[n - 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
