import math
import sys
input = sys.stdin.readline
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()

dic = dict()
for a in array:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

max_value = max(dic.values())
max_keys = []
for key in dic:
    if dic[key] == max_value:
        max_keys.append(key)




def roundCustom(x):
    isMinus = x < 0
    x = abs(x)
    ret = 0
    if (math.ceil(x) - x == x - math.floor(x)):
        ret = math.ceil(x)
    else:
        ret = round(x)
    return -ret if isMinus else ret

print(int(roundCustom(sum(array)/N)))
print(array[N//2])
print(max_keys[1] if len(max_keys) > 1 else max_keys[0])
print(max(array)-min(array))