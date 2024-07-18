N = int(input())

ans = 0
for _ in range(N):
    S = input()
    now = S[0]
    alphabets = set(now)
    for i in range(len(S)):
        c = S[i]
        if c != now:
            if c in alphabets:
                break
            else:
                now = c
                alphabets.add(c)
        if i == len(S) - 1:
            ans += 1
    
print(ans)