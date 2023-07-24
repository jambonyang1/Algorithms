n = input()
nums = [int(i) for i in n]

nums.sort()

answer = 0
for i in nums:
    if i <= 1 or answer <= 1:
        answer += i
    else:
        answer *= i

print(answer)