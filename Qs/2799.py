import sys
input = sys.stdin.readline

M, N = map(int, input().split())
table = [[0 for _ in range(N)] for _ in range(M)]
for i in range(5*M + 1):
    line = input()
    if i % 5 == 0:
        continue
    floor = i // 5
    for j in range(N):
        if line[5*j + 1] == "*":
            table[floor][j] += 1

ans = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
for line in table:
    for room in line:
        ans[room] += 1

for i in ans:
    print(ans[i], end=" ")