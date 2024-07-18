import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        candidates = [table[i][j]]
        if i > 0:
            candidates.append(table[i-1][j] + table[i][j])
        if j > 0:
            candidates.append(table[i][j-1] + table[i][j])
        table[i][j] = max(candidates)

print(table[-1][-1])