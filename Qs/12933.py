S = input()

quacks = [0, 0, 0, 0, 0]
quack_index = {"q": 0, "u": 1, "a": 2, "c": 3, "k": 4}
num = 0

for c in S:
    quacks[quack_index[c]] += 1
    for i in range(4):
        if quacks[i+1] > quacks[i]:
            num = -1
            break
    if num == -1:
        break
    else:
        num = max(quacks[0], num)
    
    if c == 'k':
        for i in range(5):
            quacks[i] -= 1

if quacks != [0, 0, 0, 0, 0]: # k가 들어올때마다 모든 값에 -1 했으니, 정상적으로 울음소리가 들렸다면 항상 [0, 0, 0, 0, 0]이 남아야 한다.
    num = -1
print(num)



# li = [0, 0, 0, 0, 0]
# index = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}

# now = 0
# max_now = 0
# for c in s:
#     if c == 'q':
#         now += 1
#         max_now = max(now, max_now)
#     elif c == 'k':
#         now -= 1
#     i = index[c]
#     li[i] += 1
#     if min(li[:i+1]) != li[i]: # li != sorted(list, reverse=True) 로 했을 땐 틀린 부분이 있었음
#         li[0] = 0
#         break

# if li[0] == 0 or not (li[0] == li[1] == li[2] == li[3] == li[4]): # 이 부분을 단순히 s가 5의 배수인지만 확인하는 것로 끝냈음. 크로스체크 제대로 하자...
#     print(-1)
# else:
#     print(max_now)