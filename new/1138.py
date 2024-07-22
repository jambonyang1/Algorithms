N = int(input())
ns = list(map(int, input().split()))

ans = [11 for _ in range(N)]
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == ns[i]:
            if ans[j] != 11:
                continue
            ans[j] = i + 1
            break
        if ans[j] > i + 1:
            cnt += 1

ans = list(map(str, ans))
print(" ".join(ans))
