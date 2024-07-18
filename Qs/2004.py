n, m = map(int, input().split())
v = 0
ii = 0
for i in range(m):
    now = n - i
    while True:
        if now % 5 == 0:
            v += 1
            now = now//5
        else:
            break
    while True:
        if now % 2 == 0:
            ii += 1
            now = now//2
        else:
            break

for i in range(1,m+1):
    while True:
        if i % 5 == 0:
            v -= 1
            i = i//5
        else:
            break
    while True:
        if i % 2 == 0:
            ii -= 1
            i = i//2
        else:
            break

print(min(v, ii))