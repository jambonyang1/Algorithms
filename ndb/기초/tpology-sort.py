from collections import deque

v, e = map(int, input().split())
indeg = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indeg[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indeg[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()