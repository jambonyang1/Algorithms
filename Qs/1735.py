A = list(map(int, input().split()))
B = list(map(int, input().split()))

c, d = A[0] * B[1] + A[1] * B[0], A[1] * B[1]

p, q = max(c, d), min(c, d)
while q != 0:
    p, q = q, p % q

c //= p
d //= p

print(c,d)