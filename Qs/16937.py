import sys
input = sys.stdin.readline

H, W = map(int, input().split())
H, W = min(H,W), max(H,W)
N = int(input())
stickers = []

for _ in range(N):
    R, C = map(int, input().split())
    R, C = min(R,C), max(R,C)
    if R <= H and C <= W:
        stickers.append([R,C])

ans = 0
N = len(stickers)
for i in range(N):
    sticker =  stickers[i]
    tmp = sticker[0] * sticker[1]
    lefts = [[H-sticker[0], W], [H, W-sticker[0]]]

    for j in range(i+1, N):
        now = stickers[j]
        for left in lefts:
            if min(now) <= min(left) and max(now) <= max(left):
                ans = max(ans, tmp + now[0] * now[1])

print(ans)