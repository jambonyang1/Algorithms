s = input()

li = [0, 0, 0, 0, 0]
index = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}

now = 0
max_now = 0
for c in s:
    if c == 'q':
        now += 1
        max_now = max(now, max_now)
    elif c == 'k':
        now -= 1
    i = index[c]
    li[i] += 1
    if min(li[:i+1]) != li[i]: # li != sorted(list, reverse=True) 로 했을 땐 틀린 부분이 있었음
        li[0] = 0
        break

if li[0] == 0 or not (li[0] == li[1] == li[2] == li[3] == li[4]): # 이 부분을 단순히 s가 5의 배수인지만 확인하는 것로 끝냈음. 크로스체크 제대로 하자...
    print(-1)
else:
    print(max_now)