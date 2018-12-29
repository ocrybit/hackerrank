#!/bin/python3
import sys

def getPrimeArr(n):
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
    return nums

def getPrimes(n):
    primes = []
    for i ,v in enumerate(getPrimeArr(n)):
        if v: primes.append(i)
    return primes

primes = getPrimes(104750)

def solve(n): return primes[n - 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
