N, M = map(int, input().split())
answer = -1
for _ in range(N):
    answer = max(min(list(map(int,input().split()))), answer)

print(answer)