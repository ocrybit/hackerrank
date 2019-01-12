#!/bin/python3
import sys

chache = {}
solutions = {}

def solve(n):
    max_chain = 0
    max_n = 0
    for n2 in range(1, n + 1):
        n3 = n2        
        chain = 1
        while n2 != 1:
            if n2 in chache:
                chain += (chache[n2] - 1)
                break
            else:
                chain += 1
                if n2 % 2 == 0:
                    n2 //= 2
                else:
                    n2 = n2 * 3 + 1
        if max_chain <= chain:
            max_chain = chain
            max_n = n3
        chache[n3] = chain
        if n3 in solutions:
            solutions[n3] = max_n
                    

arr = []
t = int(input().strip())
mx = 0

for a0 in range(t):
    n = int(input().strip())
    solutions[n] = 0
    mx = max(n, mx)
    arr.append(n)
    
solve(mx)

for n in arr:
    print(solutions[n])

