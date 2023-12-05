import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
row = [0] * N
column = [0] * M
for _ in range(Q):
    w, r, v = map(int, input().split())
    if w == 1:
        row[r-1] += v
    else:
        column[r-1] += v

for r in range(N):
    for i in range(M):
        matrix[r][i] += row[r]
for c in range(M):
    for i in range(N):
        matrix[i][c] += column[c]

for row in matrix:
    print(' '.join(map(str, row)))