import sys
input = sys.stdin.readline

K, L = map(int, input().split())
dt = dict()
for i in range(L):
    new = input().strip()
    dt[new] = i

sorted_dt = sorted(dt.items(), key= lambda x: x[1])

for i in range(min(K, len(sorted_dt))):
    print(sorted_dt[i][0])