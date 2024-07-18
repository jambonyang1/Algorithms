n = int(input())
stones = list(map(int, input().split()))

l, r = 0, 0
for st in stones:
    if l <= r:
        l += st
    else:
        r += st

diff = abs(l-r)
choos = [100, 50, 20, 10, 5, 2, 1]
ans = 0
for choo in choos:
    ans += diff // choo
    diff = diff % choo
print(ans)