#!/bin/python3
import sys

def solve(arr, t):
    r = c = 0
    paths = [(0,0)]
    s = [arr[0][0]]
    pmap = {"0-0":0}
    mx = 0
    def back():
        paths.pop()
        s.pop()
        if len(paths) == 0:
            return (-1, -1)
        r = paths[-1][0]
        c = paths[-1][1]
        pmap[str(r) + "-" + str(c)] += 1
        if pmap[str(r) + "-" + str(c)] < 2:
            r += 1
            c += 1
        elif len(paths) > 0:
            (r, c) = back()
        return (r, c)
    
    while r < t and c < len(arr[r]):
        if r == t - 1:
            mx = max(mx, sum(s))
            (r,c) = back()
        else:
            r += 1
        if r == -1:
            break
        pmap[str(r) + "-" + str(c)] = 0
        paths.append((r,c))
        s.append(arr[r][c])
    return mx

t = int(input().strip())
for a0 in range(t):
    t2 = int(input().strip())
    arr = []
    for a2 in range(t2):
        nums = [int(n2) for n2 in input().strip().split(" ")]
        arr.append(nums)
    print(solve(arr, t2))



