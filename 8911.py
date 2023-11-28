import sys
input = sys.stdin.readline

T = int(input())
directions = [[0,1], [1,0], [0,-1], [-1,0]]

for _ in range(T):
    scope = [0, 0, 0, 0] # min_x, max_x, min_y, max_y
    d = 0
    x, y = 0, 0
    case = input()
    for i in case:
        dx, dy = directions[d]
        if i == 'F':
            x, y = x+dx, y+dy
        elif i == 'B':
            x, y = x-dx, y-dy
        elif i == 'L':
            d = (d-1) % 4
        elif i == 'R':
            d = (d+1) % 4
        
        scope = [min(scope[0], x), max(scope[1], x), min(scope[2], y), max(scope[3], y)]
    print((scope[1]-scope[0])*(scope[3]-scope[2]))