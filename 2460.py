log = []
count = 0
for _ in range(10):
    out, on = map(int, input().split())
    count = count - out + on
    log.append(count)

print(max(log))