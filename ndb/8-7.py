N = int(input())

D = [0, 1, 3]
for i in range(3, N+1):
    D.append((D[i-1] + 2 * D[i-2]) % 796796)

print(D[N])