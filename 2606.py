N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 스택을 사용한 dfs
def dfs_stack():
    stack = [1]
    visited = []

    while stack:
        cur = stack.pop()
        if cur not in visited:
            visited.append(cur)
            for node in graph[cur]:
                if node not in visited:
                    stack.append(node)
    
    return len(visited) - 1

print(dfs_stack())

# 재귀 함수를 이용한 dfs
visited = [False] * (N+1)
def dfs_recursive(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(i)

dfs_recursive(1)
print(visited.count(True) - 1)