import sys
input = sys.stdin.readline

def fn(L, jewels):
    maxL = [0, 0]
    for i in range(1, L):
        m, M = maxL[0], maxL[1]
        if sum(jewels[m:M+1]) <= jewels[i]:
            if sum(jewels[m:i]) > 0:
                maxL = [m, i]
            else:
                maxL = [i, i]
        else:
            if sum(jewels[m:i+1]) > sum(jewels[m:M+1]):
                maxL = [m, i]

    return maxL[0], maxL[1]

n = int(input())
total = 0
scopes = []
for _ in range(n):
    L = int(input())
    jewels = list(map(int, input().split()))
    m, M = fn(L, jewels)
    scopes.append([m+1, M+1])
    total += sum(jewels[m:M+1])

print(total)
for scope in scopes:
    print(scope[0], scope[1])