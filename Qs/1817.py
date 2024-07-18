from collections import deque

N, M = map(int, input().split())

ans = 0
left = M
if N > 0:
    books = list(map(int, input().split()))
    for book in books:
        if book <= left:
            left -= book
        else:
            ans += 1
            left = M - book
    ans += 1
print(ans)