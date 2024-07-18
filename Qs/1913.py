N = int(input())
x = int(input())

table = [[0 for _ in range(N)] for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
d = 0
now = [N//2, N//2]
num = 1
table[now[0]][now[0]] = num
l = 1
ans = [N//2, N//2]
isBreak = False
while True:
    for _ in range(l):
        num += 1
        now[1] += dx[d]
        now[0] += dy[d]
        table[now[1]][now[0]] = num
        if num == x:
            ans[0] = now[1] + 1
            ans[1] = now[0] + 1
        elif num == N**2:
            isBreak = True
            break
    if isBreak:
        break
    d = (d+1)%4
    for _ in range(l):
        num += 1
        now[1] += dx[d]
        now[0] += dy[d]
        table[now[1]][now[0]] = num
        if num == x:
            ans[0] = now[1] + 1
            ans[1] = now[0] + 1
        elif num == N**2:
            isBreak = True
            break
    if isBreak:
        break
    d = (d+1)%4
    l += 1

for line in table:
    print(*line)
print(ans[0], ans[1])