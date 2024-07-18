import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

cases = []
fibo = [1, 1]
left = 0
for vip in vips:
    cases.append(vip-left-1)
    left = vip
cases.append(N-left)
for i in range(2, max(cases)+1):
    fibo.append(fibo[i-1]+fibo[i-2])

answer = 1
for case in cases:
    answer *= fibo[case]

print(answer)