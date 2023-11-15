import sys
input = sys.stdin.readline

N = int(input())
record = {}
answer = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a not in record:
        record[a] = [b]
        if b == 0:
            answer += 1
    else:
        if record[a][-1] == b:
            answer += 1
        record[a].append(b)

for i in record:
    if record[i][-1] == 1:
        answer += 1

print(answer)