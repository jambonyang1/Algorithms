N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

def dfs(row,col):
    if row<0 or row>=N or col<0 or col>=M:
        return False
    if graph[row][col] == 0:
        graph[row][col] = 1
        print(row, col)
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
        return True
    return False

answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            print()
            answer += 1

print(answer)