import sys
input = sys.stdin.readline

N = int(input())
logs = []
ans = 0
for i in range(N):
    new = list(map(int, input().split()))
    if new[0]:
        new[2] -= 1
        if new[2] == 0:
            ans += new[1]
        else:
            logs.append(new)
    else:
        if len(logs) == 0:
            continue
        logs[-1][2] -= 1
        if logs[-1][2] == 0:
            ans += logs[-1][1]
            logs.pop()

print(ans)