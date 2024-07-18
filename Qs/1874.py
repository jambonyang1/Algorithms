import sys
input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]

yes = True

for i in range(1, N):
    if li[i] < li[i-1]:
        for j in range(li[i]+1, li[i-1]):
            if j not in li[:i-1]:
                yes = False
                break
    if not yes:
        break


if yes:
    stack = []
    answer = []
    i = 1
    now = 0
    while now < N:
        if len(stack) == 0:
            stack.append(i)
            answer.append('+')
            i += 1
            continue

        if stack[-1] == li[now]:
            stack.pop()
            answer.append('-')
            now += 1
        else:
            stack.append(i)
            answer.append('+')
            i += 1

    print(answer)
else:
    print('NO')
