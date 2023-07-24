N = int(input())
ts = list(map(int, input().split()))

ts.sort()
answer = 0
tmp = []
for t in ts:
    if t == 1:
        answer += 1
    else:
        tmp.append(t)
        if len(tmp) >= t:
            tmp = []
            answer += 1

print(answer)