#!/bin/python3
import sys

def getPrimes(n):
    nums = list(range(2, n + 1))    
    primes = []
    while nums[0] ** 2 <= n:
        num = nums.pop(0)
        primes.append(num)
        i = 0
        while i < len(nums):
            if nums[i] % num == 0:
                nums.pop(i)
                i -= 1
            i += 1
    return primes + nums

primes = getPrimes(104729)

def solve(n): return primes[n - 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
