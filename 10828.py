import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = list(input().split())
    c = command[0]
    if c == 'push':
        stack.append(command[1])
    elif c == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])