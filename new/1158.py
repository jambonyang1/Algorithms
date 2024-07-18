N, K = map(int, input().split())

li = [i for i in range(1, N + 1)]
now = 0
ans = []
for i in range(N):
    now = (now + K - 1) % len(li)
    tmp = li[now]
    ans.append(str(tmp))
    li.remove(tmp)

print("<" + ", ".join(ans) + ">")
