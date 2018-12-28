#!/bin/python3
import math
import sys

def mapMaxTriplets(n):
    arr = []
    dic = {}
    len = 0
    for i in range(0, n+1):
        arr.append(i ** 2)
    for c in range(n, 0, -1):
        for b in range(c - 1, 1, -1):
            diff = arr[c] - arr[b]
            if diff > 0:
                a = math.sqrt(diff)
                if a == diff // a:
                    if b <= a:
                        break
                    a = int(a)
                    s = c + b + a
                    prod = c * b * a
                    if not s in dic: dic[s] = 0
                    dic[s] = max(prod, dic[s])
                    len += 1
    return dic

maxTriplets = mapMaxTriplets(3000)

def solve(n):
    if n in maxTriplets:
        return maxTriplets[n]
    else:
        return -1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
