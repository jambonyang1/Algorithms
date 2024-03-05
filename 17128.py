N, Q = map(int, input().split())
As = list(map(int, input().split()))
qs = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += As[i] * As[i-1] * As[i-2] * As[i-3]

for i in range(Q):
    q = qs[i]
    As[q-1] = -As[q-1]
    tmp = 0
    for i in range(4):
        tmp += As[(q+i-1)%N] * As[(q+i-2)%N] * As[(q+i-3)%N] * As[(q+i-4)%N]
    ans += 2 * tmp
    print(ans)




# 시간초과 걸린 코드
# li = []
# for i in range(N):
#     li.append(As[i] * As[(i+1) % N] * As[(i+2) % N] * As[(i+3) % N])

# for q in qs:
#     for i in range(4):
#         li[(q-i-1) % N] = -li[(q-i-1) % N]
#     print(sum(li))