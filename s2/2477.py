K = int(input())
sides = []
max_x, max_y = 0, 0
for i in range(6):
    d, length = map(int, input().split())
    sides.append([d, length])
    if d == 1 or d == 2:    
        max_y = max(max_y, length)
    else:
        max_x = max(max_x, length)
p = 0
for i in range(6):
    if (sides[i][1] == max_x and sides[i-1][1] == max_y) or (sides[i][1] == max_y and sides[i-1][1] == max_x):
        p = i

q = 0
for i in range(6):
    if sides[p][0] not in [sides[i-1][0], sides[i][0]] and sides[p-1][0] not in [sides[i-1][0], sides[i][0]]:
        if abs(sides[p][0] - sides[i-1][0]) == 1 and abs(sides[p-1][0] - sides[i][0]) == 1:
            q = i

print((max_x * max_y - sides[q][1] * sides[q-1][1]) * K)