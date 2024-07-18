N = int(input())
ts = list(map(int, input().split()))

ts = sorted(ts)

M = 0
if N % 2 == 0:
    for i in range(N//2):
        M = max(M, ts[i] + ts[N-i-1])
else:
    M = min(M, ts.pop())
    for i in range(N//2):
        M = max(M, ts[i] + ts[N-i-2])

print(M)