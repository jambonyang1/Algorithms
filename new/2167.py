import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum = 0
    for p in range(i - 1, x):
        for q in range(j - 1, y):
            sum += matrix[p][q]
    print(sum)
