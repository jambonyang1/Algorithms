C, R = map(int, input().split())
K = int(input())

table = [[0 for _ in range(C)] for _ in range(R)]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # up, right, down, left
x, y = 0, 0
state = 0
d = 0

if K <= C * R:
    for i in range(K):
        state += 1
        table[x][y] = state
        dir = directions[d]
        nx, ny = x + dir[0], y + dir[1]
        if nx >= R or ny >= C or nx < 0 or ny < 0:
            d = (d+1)%4
            dir = directions[d]
            nx, ny = x + dir[0], y + dir[1]
        else:
            if table[nx][ny] != 0:
                d = (d+1)%4
                dir = directions[d]
                nx, ny = x + dir[0], y + dir[1]
        
        if i != K-1:
            x, y = nx, ny
        else:
            x, y = x+1, y+1
if [x, y] == [0, 0]:
    print(0)
else:
    print(y, x)