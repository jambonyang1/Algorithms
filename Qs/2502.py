D, K = map(int, input().split())

a, b = 1, 1
for _ in range(D-3):
    a, b = b, a+b

def fn(a, b, K):
    for i in reversed(range(1, K//b+1)):
        for j in range(1, i+1):
            if i*b + j*a == K:
                return j, i

A, B = fn(a,b,K)
print(A)
print(B)