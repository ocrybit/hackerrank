#!/bin/python3
import sys
mx = 10 ** 5
lmx = 350000
nums = [True] * (lmx + 1)
sums = {}
def getPrimes(n):
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

primes = getPrimes(lmx)
memo = {}

def getFactors(n):
    num = n
    factors = [1]
    i = 0
    p = primes[i]
    s = 1
    while i < n:
        if n % p == 0:
            factors += list(map(lambda x: x * p, factors))
            factors.append(p)
            factors = list(set(factors))
            n //= p
            s *= p
            memo[s] = factors.copy()
            if not (s in sums):
                sums[s] = sum(list(set(filter(lambda x: x != s, memo[s]))))
        else:
            i += 1
            p = primes[i]
    return list(set(filter(lambda x: x != num, factors)))

def getAmicables(n):
    amicables = {}
    for i in range(n, 3, -1):
        if not nums[i]:
            if not (i in memo):
                sums[i] = sum(getFactors(i))
    sums2 = {}
    sums3 = sums.copy()
    for k, n in sums3.items():
        if n > mx and not (n in sums2):
            sums2[n] = sum(getFactors(n))
        if n != k and (n in sums and k == sums[n]) or (n in sums2 and k == sums2[n]):
            amicables[k] = n
            amicables[n] = k
    return amicables

amicables = getAmicables(mx)

def solve(n):
    s = 0
    for k, v in amicables.items():
        if k <= n:
            s += k
    return s

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))



