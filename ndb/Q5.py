N, M = map(int, input().split())
Ks = list(map(int, input().split()))

d = {i: 0 for i in range(1, M+1)}

for k in Ks:
    d[k] += 1

items = list(d.items())
answer = 0
for i in range(M):
    num = items[i][1]
    for j in range(i+1, M):
        answer += num * items[j][1]

print(answer)
