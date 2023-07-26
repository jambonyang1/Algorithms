import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, now))

dijkstra(start)

num = 0
time = 0
for i in distance:
    if i not in [0, INF]:
        num += 1
        time = max(time, i)
print(distance)
print(num, time)