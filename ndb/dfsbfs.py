# dfs, bfs 인접리스트 구현
from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def dfs(graph, v, visited): # v : 현재 노드
    visited[v] =  True
    print(v, end=' ')
    for node in graph[v]:
        if visited[node] == False:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


visited = [False] * 9
dfs(graph, 1, visited)
print('')
visited = [False] * 9
bfs(graph, 1, visited)