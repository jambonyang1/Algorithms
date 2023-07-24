from itertools import combinations as com

N = int(input())
coins = list(map(int, input().split()))


# 답지 풀이
coins.sort()

answer = 1
for coin in coins:
    if answer < coin:
        break
    answer += coin

print(answer)


# 내 풀이
# 나는 제작 가능한 모든 수를 다 만들었다.
# 하지만 문제의 핵심은 가능한 수를 찾는게 아니라 불가능한 수를 찾는 것이다.

# result = set()
# for i in range(1, N+1):
#     cases = list(com(coins, i))
#     for case in cases:
#         sum = 0
#         for i in case:
#             sum += i
#         result.add(sum)

# answer = 1
# while True:
#     if answer not in result:
#         break
#     answer += 1

# print(answer)