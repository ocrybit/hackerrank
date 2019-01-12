#!/bin/python3
import sys


def solve(n1, n2):
    c1 = n1 + n2
    c2 = c1 - max(n1, n2)
    combi = 1
    for n in range(0, c2):
        combi *= (c1 - n)
    for n in range(0, c2):
        combi //= (n + 1)
    return combi % (10 ** 9 + 7)

t = int(input().strip())
for a0 in range(t):
    s = input().strip().split(" ")
    n1 = int(s[0])
    n2 = int(s[1])
    print(solve(n1, n2))



