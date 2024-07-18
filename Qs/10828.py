import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    tmp = list(input().split())
    order = tmp[0]
    if order == "push":
        stack.append(tmp[1])
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(1 if len(stack) == 0 else 0)
    elif order == "top":
        print(-1 if len(stack) == 0 else stack[-1])
