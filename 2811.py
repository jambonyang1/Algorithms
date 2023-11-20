N = int(input())
li = list(map(int, input().split()))
li.append(0)

days = [False] * N
cnt = 0
mx_len = 0
mx_is = []
for i in range(N+1):
    if li[i] < 0:
        cnt += 1
        continue
    
    for j in range(i-3*cnt, i-cnt):
        if j >= 0:
            days[j] = True
    
    if mx_len == cnt:
        mx_is.append(i)
    elif mx_len < cnt:
        mx_len = cnt
        mx_is = [i]
    cnt = 0

ans = days.count(True)
if mx_len == 0:
    print(ans)
else:
    mx_cnt = 0
    for i in mx_is:
        cnt = 0
        for j in range(i - 4*mx_len, i - 3*mx_len):
            if j >= 0 and days[j] == False:
                cnt += 1
        if cnt > mx_cnt:
            mx_cnt = cnt
    print(ans + mx_cnt)