from collections import deque

N = int(input())
table = [list(input()) for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = []

# DFS 44ms
for i in range(N):
    for j in range(N):
        if table[i][j] == "0":
            continue
        cnt = 0
        stack = [[i, j]]
        while stack:
            x, y = stack.pop()
            if table[x][y] == "0":
                continue
            table[x][y] = "0"
            cnt += 1
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if table[nx][ny] == "1":
                        stack.append([nx, ny])
        result.append(cnt)

# BFS 68ms
# for i in range(N):
#     for j in range(N):
#         if table[i][j] == "0":
#             continue
#         queue = deque([[i, j]])
#         cnt = 0
#         while queue:
#             x, y = queue.popleft()
#             if table[x][y] == "0":
#                 continue
#             table[x][y] = "0"
#             cnt += 1
#             for dx, dy in d:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if table[nx][ny] == "1":
#                         queue.append([nx, ny])

#         result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)
