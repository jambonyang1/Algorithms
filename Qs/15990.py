import sys
input = sys.stdin.readline

T = int(input())
tests = []
for _ in range(T):
    tests.append(int(input()))

N = max(tests)
dp = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]

for i in range(4, N+1):
    one = dp[i-1][1] + dp[i-1][2]
    two = dp[i-2][0] + dp[i-2][2]
    three = dp[i-3][0] + dp[i-3][1]
    dp.append([one  % 1000000009, two  % 1000000009, three  % 1000000009])

for test in tests:
    print(sum(dp[test]) % 1000000009)