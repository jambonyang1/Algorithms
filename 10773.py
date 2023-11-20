import sys
input = sys.stdin.readline

K = int(input())
state = []
for _ in range(K):
    x = int(input())
    if x == 0:
        state.pop()
    else:
        state.append(x)

print(sum(state))