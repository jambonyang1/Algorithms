N = int(input())
eq = input()
nums = [int(input()) for _ in range(N)]
A = []
ops = []

for c in eq:
    if c.isalpha():
        A.append(nums[ord(c)-65])
        continue
    
    if len(A) > 1:
        y = A.pop()
        x = A.pop()
        if c == '+':
            A.append(x+y)
        elif c == '-':
            A.append(x-y)
        elif c == '*':
            A.append(x*y)
        elif c == '/':
            A.append(x/y)

print(f"{A[0]:.2f}")