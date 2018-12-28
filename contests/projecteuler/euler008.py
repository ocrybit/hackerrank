#!/bin/python3

import sys

def solve(n, k, num):
    mx = 0
    for i in range(0, n - k + 1):
        n2 = str(num)[i:i + k]
        prod = 1
        for i2 in range(0, k):
            prod *= int(n2[i2])
        mx = max(mx, prod)
    return mx
    
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(solve(n, k, num))
