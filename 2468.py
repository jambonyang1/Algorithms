from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
table = []
m = 101
M = 0
for _ in range(N):
    line = list(map(int, input().split()))
    table.append(line)
    m, M = min(m, min(line)), max(M, max(line))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def bfs(H):
    ret = 0
    visited = [[False]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if table[r][c] <= H or visited[r][c]:
                continue
            ret += 1
            queue = deque([[r,c]])
                   
            while queue:
                rr, cc = queue.popleft()
                if visited[rr][cc]:
                    continue
                visited[rr][cc] = True

                for i in range(4):
                    nr = rr + dr[i]
                    nc = cc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if table[nr][nc] > H and not visited[nr][nc] and [nr, nc] not in queue:
                            queue.append([nr, nc])
    return ret

ans = 1
for i in range(m, M+1):
    ans = max(ans, bfs(i))

print(ans)