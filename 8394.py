import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
fibo = [1, 1]

for i in range(2, n+1):
    fibo = [fibo[1], (fibo[0]+fibo[1]) % 10]

print(str(fibo[1])[-1])