#!/bin/python3

import sys
import math

def solve(n):
    gcd = 1
    if n == 1: return gcd
    nums = list(range(2, n + 1))
    while nums[0] ** 2 <= n:
        nums_copy = nums.copy()
        num = nums.pop(0)
        gcd *= num    
        next_pow = pow(num, 2)    
        for i in nums_copy:
            if i * num <= n:
                nums.remove(i * num)
                if next_pow == i * num:
                    gcd *= num
                    next_pow *= num
            else: break
    for i in nums:
        gcd *= i
    return gcd


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(len(str(solve(n))))
