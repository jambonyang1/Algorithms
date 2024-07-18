N, M = map(int, input().split())
mat = list()
for _ in range(N):
    mat.append(list(map(int, input().split())))

dp_mat = []
for i in range(N):
    dp_mat.append([])
    for j in range(M):
        now = mat[i][j]
        if i > 0:
            now += mat[i-1][j]
        if j > 0:
            now += mat[i][j-1]
        dp_mat[i][j] = now
K = int(input())
