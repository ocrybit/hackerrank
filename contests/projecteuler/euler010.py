#!/bin/python3
import math
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

def getPrimeSums(n):
    primes_sum = 0
    sums = []
    for i, v in enumerate(getPrimeArr(n)):
        if v: primes_sum += i
        sums.append(primes_sum)    
    return sums

sums = getPrimeSums(1000000)

def solve(n): return sums[n]
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
