import sys
input = sys.stdin.readline

N, M = map(int, input().split())

names = dict()
id = dict()
for i in range(1, N+1):
    name = input().strip()
    names[name] = i
    id[i] = name

for _ in range(M):
    tmp = input().strip()
    if tmp.isnumeric():
        print(id[int(tmp)])
    else:
        print(names[tmp])