H, W = map(int,input().split())
blocks = list(map(int,input().split()))

answer = 0
for h in range(1, H+1):
    water = 0
    isWall = False
    for b in blocks:
        if b >= h:
            if isWall:
                answer += water
            else:
                isWall = True
            water = 0
        else:
            if isWall:
                water += 1

print(answer)


# stack = []
# result = 0

# while True:
#     for w in range(len(stack)):
#         bl = blocks[w]
#         if len(stack) == 0:
#             stack.append(bl)
#             continue
#         if bl >= stack[0]:
#             for i in stack:
#                 result += stack[0] - i
#             stack = [bl]
#         else:
#             stack.append(bl)
#     blocks = list(reversed(stack))
#     stack = []
#     if len(blocks) == 0:
#         break

# print(result)