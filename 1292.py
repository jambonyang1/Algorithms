start, end = map(int, input().split())
scope = []
n = 1
while len(scope) <= 1000:
    for _ in range(n):
        scope.append(n)
    n += 1

sum = 0
for i in range(start - 1, end):
    sum += scope[i]

print(sum)