import sys

input = sys.stdin.readline
V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (V + 1)
stack = [1]
while stack:
    now = stack.pop()
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            stack.append(v)

print(visited.count(True) - 1)
