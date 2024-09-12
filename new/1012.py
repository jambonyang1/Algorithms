import sys

input = sys.stdin.readline

T = int(input())

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for _ in range(T):
    M, N, K = map(int, input().split())
    table = [[False] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, input().split())
        table[n][m] = True
    cnt = 0
    for i in range(N):
        for j in range(M):
            if table[i][j]:
                cnt += 1
                stack = [[i, j]]
                while stack:
                    r, c = stack.pop()
                    table[r][c] = False
                    for dr, dc in d:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M:
                            if table[nr][nc]:
                                stack.append([nr, nc])
    print(cnt)

# for _ in range(T):
#     M, N, K = map(int, input().split())
#     table = [[False] * M for _ in range(N)]
#     for _ in range(K):
#         x, y = map(int, input().split())
#         table[y][x] = True
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if table[i][j]:
#                 stack = [[i, j]]
#                 while stack:
#                     r, c = stack.pop()
#                     table[r][c] = False
#                     for dr, dc in d:
#                         nr, nc = r + dr, c + dc
#                         if 0 <= nr < N and 0 <= nc < M:
#                             if table[nr][nc]:
#                                 stack.append([nr, nc])
#                 cnt += 1
#     print(cnt)
