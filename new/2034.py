import sys

input = sys.stdin.readline

n = int(input())
music = []
for _ in range(n):
    music.append(int(input()))

nums = {0: "C", 2: "D", 4: "E", 5: "F", 7: "G", 9: "A", 11: "B"}

answers = []
for num in nums:
    ans = [nums[num]]
    isSuccess = True
    for m in music:
        num = (num + m) % 12
        if num not in nums:
            isSuccess = False
            break
    if isSuccess:
        ans.append(nums[num])
        answers.append(ans)

for ans in sorted(answers):
    print(" ".join(ans))
