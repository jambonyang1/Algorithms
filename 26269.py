matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))
row, col = map(int,input().split())
visited = []
cnt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c):
    if matrix[r][c] == 1:
        print(r,c)
        cnt += 1
    
    visited.append((r,c))
    if len(visited) == 4:
        if cnt >= 2:
            return True
        else:
            x, y = visited.pop()
            if matrix[x][y] == 1:
                cnt -= 1
            return False
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        ret = dfs(nr,nc)
        if ret == True:
            return True
        else:
            r, c = visited[-1]


if dfs(row, col):
    print(1)
else:
    print(0)