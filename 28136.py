N = int(input())
dishes = list(map(int, input().split()))

answer = 0
for i in range(N):
    if dishes[i] <= dishes[i-1]:
        answer += 1

print(answer)