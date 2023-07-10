H, W = map(int,input().split())
blocks = list(map(int,input().split()))

stack = []
result = 0

while True:
    for w in range(len(stack)):
        bl = blocks[w]
        if len(stack) == 0:
            stack.append(bl)
            continue
        if bl >= stack[0]:
            for i in stack:
                result += stack[0] - i
            stack = [bl]
        else:
            stack.append(bl)
    blocks = list(reversed(stack))
    stack = []
    if len(blocks) == 0:
        break

print(result)