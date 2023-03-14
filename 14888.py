from itertools import permutations
import sys
MAX = - sys.maxsize
MIN = sys.maxsize


N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

op = '+' * ops[0] + '-' * ops[1] + '*' * ops[2] + '/' * ops[3]
# set(list(permutations(op, N-1)))에서 아래 코드로 바꿨는데 시간 대폭 감소함.
# 용량이 큰 array를 list화 하는 게 시간을 많이 잡아먹는것 같음

cases = set(permutations(op))

for case in cases:
    case = [''] + list(case)

    result = nums[0]
    for i in range(1,N):
        if case[i] == '+':
            result += nums[i]
        elif case[i] == '-':
            result -= nums[i]
        elif case[i] == '*':
            result *= nums[i]
        elif case[i] == '/':
            if result < 0:
                result = -((-result) // nums[i])
            else:
                result //= nums[i]
    if result > MAX:
        MAX = result
    if result < MIN:
        MIN = result

print(MAX)
print(MIN)