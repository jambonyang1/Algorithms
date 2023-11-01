import sys
input = sys.stdin.readline

T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))

dp = [1, 1, 2, 2, 4]

mx = max(cases)
if mx > 4:
    for i in range(5, mx+1):
        value = 0
        num = i % 2
        while num <= i:
            value += dp[(i-num)//2]
            num += 2
        dp.append(value)

for case in cases:
    print(dp[case])