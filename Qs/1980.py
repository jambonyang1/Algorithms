N, M, T = map(int, input().split())
if N > M:
    N, M = M, N

ans = [T+1, -1]
for i in range(T // N, -1, -1):
    x = T - i * N
    tmp = [x % M, i + x // M]
    if ans[0] > tmp[0]:
        ans = tmp
    elif ans[0] == tmp[0]:
        if ans[1] < tmp[1]:
            ans = tmp

print(ans[1], ans[0])