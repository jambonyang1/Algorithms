N = input()
nums = dict()
for i in range(9):
    nums[str(i)] = 0
for n in N:
    if n == "9":
        nums["6"] += 1
    else:
        nums[n] += 1

nums["6"] = (nums["6"] + 1) // 2


if max(nums.values()) == 0:
    print(1)
else:
    print(max(nums.values()))
