import sys

input = sys.stdin.readline
N = int(input())
array = []
for _ in range(N):
    num = int(input())
    if len(array) == 0:
        array.append(num)
    else:
        inserted = False
        for i in range(len(array)):
            if num <= array[i]:
                array.insert(i, num)
                inserted = True
                break
        if not inserted:
            array.append(num)

print(int(round(sum(array) / N, 0)))
print(array[N // 2])

freqs = dict()
for i in array:
    if i in freqs:
        freqs[i] += 1
    else:
        freqs[i] = 1

mf = 0
ans = []
for key in freqs:
    if freqs[key] > mf:
        ans = [key]
        mf = freqs[key]
    elif freqs[key] == mf:
        ans.append(key)
if len(ans) > 1:
    print(ans[1])
else:
    print(ans[0])
print(array[-1] - array[0])
# array.sort()

# dic = dict()
# for a in array:
#     if a in dic:
#         dic[a] += 1
#     else:
#         dic[a] = 1

# max_value = max(dic.values())
# max_keys = []
# for key in dic:
#     if dic[key] == max_value:
#         max_keys.append(key)


# def roundCustom(x):
#     isMinus = x < 0
#     x = abs(x)
#     ret = 0
#     if (math.ceil(x) - x == x - math.floor(x)):
#         ret = math.ceil(x)
#     else:
#         ret = round(x)
#     return -ret if isMinus else ret

# print(int(roundCustom(sum(array)/N)))
# print(array[N//2])
# print(max_keys[1] if len(max_keys) > 1 else max_keys[0])
# print(max(array)-min(array))
