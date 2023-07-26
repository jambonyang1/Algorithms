import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V + 1)

for _ in range(E):
    fr, to, dist = map(int, input().split())
    graph[fr].append((to, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance)