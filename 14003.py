import sys
input = sys.stdin.readline

N = int(input())
array = list(set(map(int, input().split())))
N = len(array)
def return_list(n):
    return([n])
dp = list(map(return_list, array))

maxList = []
for i in range(0, N-1):
    for j in range(i+1, N):
        if array[i] < array[j]:
            if len(dp[j]) < len(dp[i]) + 1:
                dp[j] = dp[i] + [array[j]]
                maxList = maxList if len(maxList) > len(dp[j]) else dp[j]
print(array)
print(len(maxList))
print(maxList)

# https://www.acmicpc.net/source/54787343 에서 힌트 얻기