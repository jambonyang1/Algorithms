N = int(input())

dp = [0, 0, 1, 3]

def dynamic(N):
    if N < 4:
        return dp[N]
    half = N // 2
    if half == N - half:
        return 2 * dynamic(half) + half*(N-half)
    else:
        return dynamic(half) + dynamic(N - half) + half*(N-half)

print(dynamic(N))

# dp = [0, 0]

# for i in range(2, N+1):
#     half = i // 2
#     dp.append(dp[half] + dp[i - half] + half * (i-half))

# print(dp[N])