N = int(input())
moves = list(input().split())

x, y = 1, 1

# L, R, U, D
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mv_types = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(4):
        if move == mv_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue

    x = nx
    y = ny

print(y, x)


# row, column = 1, 1
# for mv in moves:
#     if mv == 'R' and column != N:
#         column += 1
#     elif mv == 'L' and column != 1:
#         column -= 1
#     elif mv == 'U' and row != 1:
#         row -= 1
#     elif mv == 'D' and row != N:
#         row += 1

# print(row, column)