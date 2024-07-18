N = int(input())
a = [i for i in list(map(int, input().split())) if i != 0]
table = [a.count(2 ** i) for i in range(64)]

ans = 0
for i in range(63):
    if table[i] != 0:
        ans = i
    table[i+1] += table[i] // 2

print(2 ** ans)