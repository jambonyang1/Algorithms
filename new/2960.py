N, K = map(int, input().split())

li = [i for i in range(2, N + 1)]
rm = 2
tmp = 2
cnt = 0
while True:
    if rm > N:
        rm = li[0]
        tmp = li[0]
        li.remove(rm)
        cnt += 1
    elif rm in li:
        li.remove(rm)
        cnt += 1
    if cnt == K:
        break
    rm += tmp

print(rm)
