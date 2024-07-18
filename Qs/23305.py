import sys
input = sys.stdin.readline

N = int(input())
d = [0] * 1000001

A = list(map(int, input().split()))
for i in A:
    d[i] += 1

B = list(map(int, input().split()))
for i in B:
    if d[i] >= 1:
        d[i] -= 1

print(sum(d))