N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs():
    stack = [[0, 0]]
    visited = []

    while stack:
        x, y = stack.pop()
        if  [x, y] in visited:
            continue
        visited.append([x, y])
        step = graph[x][y]
        if x+step < N:
            stack.append([x+step, y])
        if y+step < N:
            stack.append([x, y+step])
    if [N-1, N-1] in visited:
        return True
    else:
        return False

print("HaruHaru" if dfs() else "Hing") 
