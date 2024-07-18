brackets = list(input())

stack = list()
result = 0
res = 1

for i in range(len(brackets)):
    brac = brackets[i]
    if brac == '(':
        res *= 2
        stack.append(brac)
    elif brac == '[':
        res *= 3
        stack.append(brac)
    elif brac == ')':
        if len(stack) == 0 or stack[-1] == '[':
            result = 0
            break
        if brackets[i-1] == '(':
            result += res

        res //= 2
        stack.pop()
    elif brac == ']':
        if len(stack) == 0 or stack[-1] == '(':
            result = 0
            break
        if brackets[i-1] == '[':
            result += res

        res //= 3
        stack.pop()

# ((()) 이런 경우는 위의 for문에서 에러가 탐지가 안된다. 그래서 마지막으로 stack에 아이템이 있는지 체크해봐야 함
if len(stack) != 0:
    print(0)
else:
    print(result)