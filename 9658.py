N = int(input())

dp = [1, 0, 1, 0]

def name(value):
    if value:
        return "SK"
    else:
        return "CY"

for i in range(4, N+1):
    if dp[i-1] and dp[i-3] and dp[i-4]: # SK가 지는 경우의 수만 있는 경우에만 CY가 이기고
        dp.append(0)
    else: # 이외엔 전부 SK가 이긴다. 선으로 두는 사람이 절대적으로 유리한 게임
        dp.append(1)

print(name(dp[N]))