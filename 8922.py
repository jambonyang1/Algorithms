import sys
input = sys.stdin.readline

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    li = list(map(int, input().split()))
    tmp = li[:]
    records = [tmp[:]]
    while True:
        for i in range(n):
            tmp.append(abs(tmp[i]- tmp[(i+1)%n]))
        tmp = tmp[n:]
        if min(tmp) == max(tmp) == 0:
            results.append("ZERO")
            break
        if tmp in records:
            results.append("LOOP")
            break
        records.append(tmp[:])

for result in results:
    print(result)