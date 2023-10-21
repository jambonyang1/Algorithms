import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(1, N):
    table[i][0] += table[i-1][0]
for j in range(1, M):
    table[0][j] += table[0][j-1]

for i in range(1, N):
    for j in range(1, M):     
        table[i][j] += max(table[i][j-1], table[i-1][j])

print(table[N-1][M-1])