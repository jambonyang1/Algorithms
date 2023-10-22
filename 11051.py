N, K = map(int, input().split())

def fn(m, M):
    ret = 1
    for i in range(m, M+1):
        ret *= i
    return ret

print((fn(N-K+1, N) // fn(1, K)) % 10007)