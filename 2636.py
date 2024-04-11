import sys
input = sys.stdin.readline
H, W = map(int, input().split())
table = []
total = 0
for _ in range(H):
    li = list(map(int, input().split()))
    total += li.count(1)
    li[0], li[-1] = 2, 2
    table.append(li)
table[0], table[-1] = [2] * W, [2] * W
dr = [0, 1, 0, -1]
dc = [1, 0 ,-1, 0]

def air(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if table[nr][nc] == 2:
            return True
    return False

def change(target):
    cnt = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            a = air(i, j)
            if target == 1 and table[i][j] == 1 and a:
                table[i][j] = 3
            elif target == 3 and table[i][j] == 3:
                table[i][j] = 2
                cnt += 1
    return cnt

def zero_to_two():
    for i in range(1, H-1):
        for j in range(1, W-1):
            if table[i][j] == 0 and air(i, j):
                stack = [[i, j]]
                while stack:
                    r, c = stack.pop()
                    table[r][c] = 2
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if table[nr][nc] == 0:
                            stack.append([nr, nc])

time = 0
while total > 0:
    deleted = change(3)
    if total == deleted:
        print(time)
        print(total)
        break
    total -= deleted
    zero_to_two()
    change(1)
    time += 1