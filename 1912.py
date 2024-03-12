N = int(input())
series = list(map(int, input().split()))

# 새로운 풀이
ans = -1e9
now = -1e9
for i in series:
    if now < 0:
        now = i
    else:
        now += i
    ans = max(ans, now)

print(ans)


# 이전 풀이
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