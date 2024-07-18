table = [
    ["***", "* *", "* *", "* *", "***"],
    ["  *", "  *", "  *", "  *", "  *"],
    ["***", "  *", "***", "*  ", "***"],
    ["***", "  *", "***", "  *", "***"],
    ["* *", "* *", "***", "  *", "  *"],
    ["***", "*  ", "***", "  *", "***"],
    ["***", "*  ", "***", "* *", "***"],
    ["***", "  *", "  *", "  *", "  *"],
    ["***", "* *", "***", "* *", "***"],
    ["***", "* *", "***", "  *", "***"],
]


nums = []
for _ in range(5):
    nums.append(input())
k = (len(nums[0]) + 1) // 4
total = 0
isEven = False
for i in range(k):
    tmp = []
    for j in range(5):
        tmp.append(nums[j][4*i:4*i+3])
    for j in range(10):
        if tmp == table[j]:
            total += j
            if i == k -1:
                isEven = j % 2 == 0
            break


print("BEER!!" if total % 3 == 0 and isEven else "BOOM!!")