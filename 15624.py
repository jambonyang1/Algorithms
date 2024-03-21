N = int(input())

a, b = 0, 1
m = 1000000007
for i in range(N):
    a, b = b%m, (a+b)%m

print(a)