ns = input()

answer = {'0': 0, '1': 0}
now = ns[0]
answer[now] += 1
for n in ns:
    if n != now:
        answer[n] += 1
        now = n
print(min(answer['0'], answer['1']))