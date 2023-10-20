n = int(input())
array = list(map(int, input().split()))

pos = 0
max_value = min(array)
for i in array:
    if pos + i >= 0:
        pos += i
        max_value = max(max_value, pos)
    else:
        pos = 0
        max_value = max(max_value, i)

print(max_value)