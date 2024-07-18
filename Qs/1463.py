X = int(input())
dp = [0] * (X+1)

def recursive(n):
    if dp[n] != 0 or n < 2:
        return dp[n]
    cdds = [recursive(n-1)]
    if n % 2 == 0:
        cdds.append(recursive(n//2))
    if n % 3 == 0:
        cdds.append(recursive(n//3))
    dp[n] = min(cdds)+1
    return dp[n]

print(recursive(X))
# dp = [0, 0]
# for i in range(2, X+1):
#     cdds = [dp[i-1]+1]
#     if i%2 == 0:
#         cdds.append(dp[i//2]+1)
#     if i%3 == 0:
#         cdds.append(dp[i//3]+1)
#     dp.append(min(cdds))    

# print(dp[X])


# MAX = X + 1
# d = [0] * MAX

# for i in range(2, MAX):
#     tmp = [d[i-1]+1]
#     if i % 2 == 0:
#         tmp.append(d[i//2]+1)
#     if i % 3 == 0:
#         tmp.append(d[i//3]+1)
#     d[i] = min(tmp)

# print(d[X])