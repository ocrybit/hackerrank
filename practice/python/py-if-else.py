#!/bin/python3

N = int(input())
if N % 2 != 0 or (6 <= N and N <= 20):
    print("Weird")
else:
    print("Not Weird")
