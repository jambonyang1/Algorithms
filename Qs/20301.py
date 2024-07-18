N, K, M = map(int, input().split())

now = K - 1
state = 0
direction = 1
li = [i for i in range(1, N+1)]

for i in range(1, N+1):
    print(li[now])
    del li[now]
    if i == N:
        break
    if i % M == 0:
        direction = - direction
    now = (now + direction * (K - 1)) % len(li) if direction == 1 else (now + direction * K) % len(li)