ans = [0, 0]
for i in range(1, 10):
    n = int(input())
    if n > ans[0]:
        ans = [n, i]

for n in ans:
    print(n)