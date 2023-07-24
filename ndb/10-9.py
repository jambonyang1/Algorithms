from collections import deque
import copy

N = int(input())

indeg = [0] * (N+1)
graph = [[] for _ in range(N+1)]
cost = [0] * (N+1)

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    cost[i] = tmp[0]
    for x in tmp[1:]:
        indeg[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(cost)
    q = deque()

    for i in range(1, N+1):
        if indeg[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + cost[i])
            indeg[i] -= 1

            if indeg[i] == 0:
                q.append(i)
    
    for i in range(1, N+1):
        print(result[i])

topology_sort()    

