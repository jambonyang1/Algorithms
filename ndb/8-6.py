N = int(input())
D = list(map(int, input().split()))

for i in range(2, N):
    tmp = [D[i]]
    if i-2 >= 0:
        tmp.append(D[i] + D[i-2])
    if i-3 >= 0:
        tmp.append(D[i] + D[i-3])
    D[i] = max(tmp)

print(D)