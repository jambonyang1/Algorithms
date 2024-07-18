from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    d = deque(list(map(int, input().split())))
    tmp_max = max(d)
    count = 0
    while True:
        back = d.popleft()
        if back < tmp_max:
            d.append(back)
            if M == 0:
                M = len(d) - 1
            else:
                M -= 1
        else:
            count += 1
            if M == 0:
                print(count)
                break
            M -= 1
            tmp_max = max(d)
