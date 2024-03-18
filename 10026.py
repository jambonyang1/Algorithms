N = int(input())
RGB = []
RB = []
for _ in range(N):
    line = input()
    RGB.append(list(line))
    line.replace('G', 'R')
    RB.append(list(line.replace('G', 'R')))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(table):
    ans = 0
    for r in range(N):
        for c in range(N):
            if table[r][c] == 'X':
                continue
            ans += 1
            stack = [[r,c]]
            color = table[r][c]
            while stack:
                now = stack.pop()
                table[now[0]][now[1]] = 'X'
                for i in range(4):
                    nr = now[0]+dr[i]
                    nc = now[1]+dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if table[nr][nc] == color:
                            stack.append([nr, nc]) 
    return ans

print(dfs(RGB), dfs(RB))