N, K = map(int, input().split())
answer = 0
while True:
    answer += 1
    if N % K == 0:
        N = N // K
    else:
        N -= 1
    if N == 1:
        break

print(answer)