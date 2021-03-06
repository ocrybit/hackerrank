#!/bin/python3

import sys
import itertools

def solve (grid):
    def prod(i, i2, a1, a2, n = 0): return 1 if n > 3 else grid[i + (n * a1)][i2 + (n * a2)] * prod(i, i2, a1, a2, n + 1)
    mx = 0
    for i, i2 in itertools.product(range(0, 20), range(0, 17)):
        mx = max(mx, prod(i, i2, 0, 1), prod(i2, i, 1, 0))
        if i < 17: mx = max(mx, prod(i, i2, 1, 1), prod(i, 19 - i2, 1, -1))
    return mx            

grid = []
for grid_i in range(20):
 grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
 grid.append(grid_t)
print(solve(grid))
