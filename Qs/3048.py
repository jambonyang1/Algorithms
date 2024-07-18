pn, sn = map(int, input().split())
p = list(input())
s = list(input())
stop = int(input())

p.reverse()
state = p + s

end = pn + sn - 1 # -1을 해주는 이유는 indexerror 때문
for _ in range(stop):
    i = 0
    while i < end:
        if state[i] in p and state[i+1] in s:
            state[i], state[i+1] = state[i+1], state[i]
            i += 2
        else:
            i += 1

print(''.join(state))