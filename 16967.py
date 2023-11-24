import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
A = []
B = []
for i in range(H+X):
    line = list(map(int, input().split()))
    if i < H:
        A.append(line[:W])
    B.append(line)

for i in range(H-X):
    for j in range(W-Y):
        A[i + X][j + Y] -= A[i][j]

for l in A:
    print(' '.join(map(str, l)))