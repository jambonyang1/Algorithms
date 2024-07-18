Y, X = map(int, input().split())

ans = 1
if Y == 2:
    ans += min((X - 1) // 2, 3)
elif Y > 2:
    if X < 7:
        ans += min(X - 1, 3)
    else:
        ans += X - 1 - 2

print(ans)