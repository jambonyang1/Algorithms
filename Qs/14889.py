from itertools import combinations
N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

cases = combinations([i for i in range(N)], N // 2)
ans = 1e9
for cs in cases:
    numOne = 0
    numTwo = 0
    for i in range(N):
        if i in cs:
            for j in cs:
                numOne += table[i][j]
        else:
            for j in range(N):
                if j not in cs:
                    numTwo += table[i][j]
    ans = min(ans, abs(numOne - numTwo))

print(ans)