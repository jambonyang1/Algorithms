from math import factorial as fac
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fac(M) // fac(N) // fac(M-N))