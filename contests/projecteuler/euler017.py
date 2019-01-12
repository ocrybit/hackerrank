#!/bin/python3
import sys

def toStr(n):
    num_str = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    arr = []
    narr = list(n)
    if int(n) >= 100:
        n2 = narr.pop(0)
        arr.append(num_str[int(n2) - 1])
        arr.append("Hundred")
    if len(narr) == 3:
        narr.pop(0)
    narr_int = int("".join(narr))
    if narr_int < 20 and narr_int != 0:
        arr.append(num_str[narr_int - 1])
    else:
        if int(narr[0]) != 0:
            arr.append(tens[int(narr[0]) - 2])
        if int(narr[1]) != 0:            
            arr.append(num_str[int(narr[1]) - 1])
    return " ".join(arr)

def solve(n):
    if n == 0:
        return "Zero"
    units = ["Thousand", "Million", "Billion", "Trillion"]
    arr = []
    mod = len(str(n)) % 3
    if mod == 0:
        mod = 3
    ceil = -(-len(str(n)) // 3)
    for n2 in range(1, ceil + 1):
        if n2 == 1:
            nums = str(n)[0 : mod]
        else:
            first = mod + (n2 - 2) * 3
            nums = str(n)[first : first + 3]
        if int(nums) != 0:
            arr.append(toStr(nums))
            if n2 != ceil:
                arr.append(units[ceil - n2 - 1])
    return " ".join(arr)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))        


