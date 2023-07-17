X = int(input())
MAX = X + 1
d = [0] * MAX

for i in range(2, MAX):
    tmp = [d[i-1]+1]
    if i % 2 == 0:
        tmp.append(d[i//2]+1)
    if i % 3 == 0:
        tmp.append(d[i//3]+1)
    d[i] = min(tmp)

print(d[X])