#!/bin/python3
import sys
def day(y, m, d): return (y + (y // 4) - (y // 100) + (y // 400) + (((13 * m) + 8) // 5) + d) % 7
def solve(d1, d2):
    n1 = d1
    n2 = d2
    if n1[0] == n2[0] and (n1[1] > n2[1] or (n1[1] == n2[1] and n1[2] > n2[2])): d1, d2 = n2, n1
    s = 0
    for year in range(n1[0], n2[0] + 1):
        for month in range(1, 13):
            if year == n1[0] and month < n1[1]: continue
            if month < 3:
                y = year - 1
                m = month + 12
            else:
                y = year
                m = month
            if year >= n2[0] and month > n2[1]: break
            if year == n1[0] and month == n1[1] and n1[2] != 1: continue
            if day(y, m, 1) == 0: s += 1
        if y >= n2[0]: break            
    return s

t = int(input().strip())
for a0 in range(t):
    n1 = [int(n) for n in input().strip().split(" ")]
    n2 = [int(n) for n in input().strip().split(" ")]
    print(solve(n1, n2))



