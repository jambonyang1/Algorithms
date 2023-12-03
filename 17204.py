import sys
input = sys.stdin.readline

N, K = map(int, input().split())
target = []
for _ in range(N):
    target.append(int(input()))

now = 0
graph = []
while True:
    if now in graph:
        break
    graph.append(now)
    if now == K:
        break
    now = target[now]

if K in graph:
    print(len(graph)-1)
else:
    print(-1)