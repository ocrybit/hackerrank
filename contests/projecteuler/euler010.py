#!/bin/python3
import math
import sys

def getPrimeSums(n):
    nums = [None] * (n + 1)
    nums[0] = False
    nums[1] = False
    prime_sum = 0
    sums = [0, 0]
    i = 2
    while i <= n:
        if nums[i] != False:
            nums[i] = True
            prime_sum += i
            prod = i * 2
            while prod <= n:
                nums[prod] = False
                prod += i
        sums.append(prime_sum)
        i += 1
    return sums


sums = getPrimeSums(10 ** 6)

def solve(n): return sums[n]
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
