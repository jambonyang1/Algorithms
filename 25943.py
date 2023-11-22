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
while diff > 0:
    for ch in choos:
        if diff >= ch:
            diff -= ch
            ans += 1
            break
    
print(ans)