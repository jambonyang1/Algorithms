import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
total = B
blocks = []
low, high = 1e9, -1
for _ in range(N):
    line = list(map(int, input().split()))
    total += sum(line)
    blocks.append(line)
    low = min(low, min(line))
    high = max(high, max(line))
mx = total // (N * M)
ans = 1e9
height = low
for i in reversed(range(low, min(mx, high) + 1)):
    tmp = 0
    for p in range(N):
        for q in range(M):
            now = blocks[p][q]
            if now > i:
                tmp += (now - i) * 2
            else:
                tmp += i - now
    if ans > tmp:
        ans = tmp
        height = i
    else:
        break

print(ans, height)
