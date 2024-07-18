A, K = map(int, input().split())


# 계산
# 더 빠름
count = 0
x = K

while x != A:
    count += 1
    if x % 2 == 0:
        if x // 2 >= A:
            x //= 2
        else:
            x -= 1
    else:
        x -= 1


print(count)



# 다이나믹 프로그래밍
dp = [0]

for i in range(A + 1, K + 1):
    if i % 2 == 0:
        if i // 2 >= A:
            dp.append(min(dp[i - 1 - A], dp[i // 2 - A]) + 1)
        else:
            dp.append(dp[i - 1 - A] + 1)
    else:
        dp.append(dp[i - 1 - A] + 1)

print(dp[-1])