import sys
input = sys.stdin.readline

values = [[1, 1], [1, 2], [1, 3], [1, 2], [1, 3], [1, 4], [1, 3], [1, 3], [1, 3], [1, 2]]
dial = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [0, 4, 8], [5, 7, 9], [6, 8]]

T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))

mx = max(cases)
for a in range(mx-2):
    for i in range(10):
        tmp = 0
        for j in dial[i]:
            tmp = (tmp + values[j][a+1]) % 1234567
        values[i].append(tmp)

results = [0] * mx
for val in values:
    for i in range(mx):
        results[i] = (results[i] + val[i]) % 1234567

for case in cases:
    print(results[case-1] )