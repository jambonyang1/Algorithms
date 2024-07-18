N = int(input())
S = input()

d = [[0, -1], [-1, 0], [0, 1], [1, 0]]
now = 0
log = [[0, 0]]
min_x, min_y = 0, 0
for s in S:
    if s == 'R':
        now = (now + 1) % 4
    elif s == 'L':
        now = (now - 1) % 4
    else:
        dx, dy = d[now]
        new = [log[-1][0]+dx, log[-1][1]+dy]
        min_x, min_y = min(min_x, new[0]), min(min_y, new[1])
        log.append(new)

max_x, max_y = 0, 0
log = sorted(log, key=lambda x: [x[0], x[1]])
for i in range(len(log)):
    log[i][0] -= min_x
    log[i][1] -= min_y
    max_x, max_y = max(max_x, log[i][0]), max(max_y, log[i][1])

table = [['#' for _ in range(max_x+1)] for _ in range(max_y+1)]
for x, y in log:
    table[y][x]  = '.'

for line in reversed(table):
    print(''.join(line))