#!/bin/python3

import sys

def getPrimes(n):
    nums = [True] * (n + 1)
    nums[0] = False
    nums[1] = False
    i = 2
    while i ** 2 <= n:
        if nums[i] != False:
            nums[i] = True
            prod = i * 2
            while prod <= n:
                nums[prod] = False
                prod += i
        i += 1
    primes = []
    for num, isPrime in enumerate(nums):
        if isPrime:
            primes.append(num)
    return primes

primes = getPrimes(41039)

def getFactors(n):
    factors = {}
    i = 0
    p = primes[i]
    while i < n:
        if n % p == 0:
            n //= p
            factors.setdefault(p,0)
            factors[p] += 1
        else:
            i += 1
            p = primes[i]
    return factors

def combi(factors):
    c = 1
    for n in factors.values():
        c *= (n + 1)
    return c

def getSolutions(n):
    max_num_factors = 1
    solutions = [0]
    triangle_sum = 1
    num = 2
    while max_num_factors <= n:
        triangle_sum += num
        factors = getFactors(triangle_sum)
        c = combi(factors)
        if max_num_factors < c:
            max_num_factors = max(max_num_factors, c)
            while len(solutions) < max_num_factors:
                solutions.append(triangle_sum)
        num += 1
    return solutions

solutions = getSolutions(10 ** 3)

def solve(n):
    return solutions[n]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
