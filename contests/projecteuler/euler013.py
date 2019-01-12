#!/bin/python3

import sys

s = 0
t = int(input().strip())
for a0 in range(t):s += int(input().strip())
print(str(s)[0:10])
