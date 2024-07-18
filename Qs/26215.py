N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
ans = 0
while len(a) > 1:
    a[0] -= 1
    a[1] -= 1
    a = sorted([i for i in a if i > 0], reverse=True)
    ans += 1

if len(a) == 1:
    ans += a[0]

if ans > 1440:
    print(-1)
else:
    print(ans)