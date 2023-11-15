import sys
input = sys.stdin.readline

t, x, m = map(int, input().split())
avail = 1e9
for _ in range(m):
    d, s = map(int, input().split())
    tmp = d // s
    if d % s == 0:
        tmp -= 1
    avail = min(avail, tmp)

if avail >= t:
    print(t*x)
else:
    if avail == 0:
        print(0)
    else:
        print(avail*x + ((t-avail)//2)*x)