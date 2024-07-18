card = list(input().split())

def min_card(li):
    a, b, c, d = li
    return min(int(a+b+c+d), int(b+c+d+a), int(c+d+a+b), int(d+a+b+c))

ans = 0
target = min_card(card)
for i in range(1111, target+1):
    if i == min_card(list(str(i))):
        ans += 1

print(ans)