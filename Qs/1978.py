N = int(input())
nums = list(map(int, input().split()))
MAX = 1000


scope = [i for i in range(2, MAX + 1)]
primes = []
while len(scope) > 0:
    prime = scope[0]
    primes.append(prime)
    for i in range(2, MAX + 1):
        if i % prime == 0:
            if i in scope:
                scope.remove(i)

count = 0
for num in nums:
    if num in primes:
        count += 1

print(count)