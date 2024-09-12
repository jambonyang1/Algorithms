N, M = map(int, input().split())
avail = list(map(int, input().split()))

un = [0]
for i in range(1, N + 1):
    if i not in avail:
        un.append(i)

answer = 0
for i in range(1, len(un)):
    if i == 1:
        answer += 7
    else:
        answer += min(7, 2 * (un[i] - un[i - 1]))

print(answer)
