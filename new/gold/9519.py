X = int(input())
org = input()
l = len(org)
front = l // 2 + l % 2
back = l - front
li = [org]
while True:
    s = li[-1]
    a = s[:front]
    b = s[front:]
    tmp = []
    for i in range(back):
        tmp.append(a[i])
        tmp.append(b[-i - 1])
    if front > back:
        tmp.append(a[-1])
    new_s = "".join(tmp)
    if new_s == org:
        break
    li.append(new_s)

print(li[-X % len(li)])
