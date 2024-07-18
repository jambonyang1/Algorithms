N, M = map(int, input().split())
tiles = [input() for _ in range(N)]

ans = 0
for tile in tiles:
    isHorizontal = False
    for i in tile:
        if i == '-':
            if not isHorizontal:
                ans += 1
                isHorizontal = True
        else:
            isHorizontal = False

for i in range(M):
    isVertical = False
    for j in range(N):
        if tiles[j][i] == '|':
            if not isVertical:
                ans += 1
                isVertical = True
        else:
            isVertical = False

print(ans)