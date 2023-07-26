import sys
input = sys.stdin.readline
INF = int(1e9)

V = int(input())
E = int(input())

graph = [[INF] * (V+1) for _ in range(V+1)]
for i in range(E):
    fr, to, dist = map(int, input().split())
    graph[fr][to] = dist

for i in range(1, V+1):
    graph[i][i] = 0

for th in range(1, V+1):
    for fr in range(1, V+1):
        for to in range(1, V+1):
            graph[fr][to] = min(graph[fr][to], graph[fr][th] + graph[th][to])
    
for i in graph:
    print(i)
