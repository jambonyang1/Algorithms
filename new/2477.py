K = int(input())
log = []
H, V = 0, 0
for _ in range(6):
    a, l = map(int, input().split())
    log.append([a, l])
    if a == 1 or a == 2:
        V = max(V, l)
    else:
        H = max(H, l)

hex = []
now = 0
while True:
    if log[now][0] in hex:
        hex.append(log[now][0])
    else:
        if len(hex) > 0:
            hex = [hex[-1], log[now][0]]
        else:
            hex = [log[now][0]]
    if len(hex) == 4:
        break
    now = (now + 1) % 6

h, v = log[now - 1][1], log[now - 2][1]

print((H * V - h * v) * K)
