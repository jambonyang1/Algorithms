N = int(input())
final = list()
nums = input().split()
for num in nums[:N]:
    num = int(num)
    if (num ** 0.5) ** 2 == num:
        final.append(1)
    else:
        final.append(0)
print(*final)