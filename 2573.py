import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
minus_table = [[0]*M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs():
    total = 0
    stack = []
    visited = [[False]*M for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, M-1):
            if visited[i][j] or table[i][j] == 0:
                continue
            total += 1
            if total > 1:
                return -1
            stack = [[i, j]]
            visited[i][j] = True
            while stack:
                r, c = stack.pop()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if table[nr][nc] != 0 and not visited[nr][nc]:
                        stack.append([nr, nc])
                        visited[nr][nc] = True
                    elif table[nr][nc] == 0:
                        minus_table[r][c] += 1
    if total == 0:
        return 0
    return 1

day = 0
while True:
    for i in range(1, N-1):
        for j in range(1, M-1):
            table[i][j] -= min(minus_table[i][j], table[i][j])
            minus_table[i][j] = 0
    
    result = dfs()
    if result == -1:
        print(day)
        break
    elif result == 0:
        print(0)
        break
    
    day += 1



























# def dfs():
#     while True:
#     count = 0
#     visited = []
#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             if table[i][j] == 0 or [i, j] in visited:
#                 continue
#             count += 1
#             if count > 1:
#                 return 1
#             stack = [[i,j]]

#             while stack:
#                 now = stack.pop()
#                 if now in visited:
#                     continue
#                 visited.append(now)

#                 for i in range(4):
#                     nr = now[0]+dr[i]
#                     nc = now[1]+dc[i]
#                     if table[nr][nc] != 0:
#                         stack.append([nr, nc])
#     if count == 0:
#         return 0
#     else:
#         return -1

    

# def function():
#     ans = 0
#     minus_table = [[0 for _ in range(M)] for _ in range(N)]    
#     while True:
#         for i in range(1, N-1):
#             for j in range(1, M-1):
#                 table[i][j] -= minus_table[i][j]
#                 minus_table[i][j] = 0
#         result = dfs()
#         if result == 0:
#             return 0
#         elif result == 1:
#             return ans
        
#         for i in range(1, N-1):
#             for j in range(1, M-1):
#                 if table[i][j] == 0:
#                     continue
#                 sea = 0
#                 for k in range(4):
#                     if table[i+dr[k]][j+dc[k]] == 0:
#                         sea += 1
#                 if sea == 4:
#                     return ans
#                 minus_table[i][j] += min(table[i][j], sea)
#         ans += 1

# print(function())