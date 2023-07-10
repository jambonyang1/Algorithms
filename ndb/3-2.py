N, M, K = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

answer = 0
cnt = 0
for _ in range(M):
    if cnt == K:
        answer += arr[1]
        cnt = 0
    else:
        answer += arr[0]
        cnt += 1

print(answer)
