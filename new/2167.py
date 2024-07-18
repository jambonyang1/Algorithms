import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in reversed(range(M)):
        matrix[i][j] = sum(matrix[i][: j + 1])
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum = 0
    for p in range(i - 1, x):
        if j == 1:
            sum += matrix[p][y - 1]
        else:
            sum += matrix[p][y - 1] - matrix[p][j - 2]
    print(sum)
