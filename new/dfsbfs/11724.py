import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
ans = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    ans += 1
    stack = [i]
    while stack:
        now = stack.pop()
        visited[now] = True
        for v in graph[now]:
            if not visited[v]:
                stack.append(v)

print(ans)
