N = int(input())

D = [0, 1, 2]
for i in range(3, N+1):
    D.append(D[i-1] + D[i-2])

print(D[N] % 10007)