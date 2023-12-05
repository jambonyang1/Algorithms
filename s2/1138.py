N = int(input())
li = list(map(int, input().split()))
ans = [-1] * N
for i in range(N): # li를 iterate
    tmp = 0
    for j in range(N): # ans를 iterate
        if ans[j] == -1:
            if tmp == li[i]:
                ans[j] = i + 1
                break
            else:
                tmp += 1

print(' '.join(map(str, ans)))