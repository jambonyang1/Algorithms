N = int(input())
M = int(input())

# 에라토스테네스의 체 구현 개선 필요
# MAX 값이 커질수록 시간 기하급수적으로 증가하는 듯
# 시간 복잡도 계산해서 재구현
MAX = M
scope = [i for i in range(2, MAX + 1)]
primes = []
while len(scope) > 0:
    prime = scope[0]
    if prime >= N and prime <= M:
        primes.append(prime)
    for i in range(2, MAX + 1):
        if i % prime == 0:
            if i in scope:
                scope.remove(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))