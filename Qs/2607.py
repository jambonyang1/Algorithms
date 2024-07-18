N = int(input())
S = list(input())
S_set = set(S)
ans = 0
for _ in range(N-1):
    n = list(input())
    n_set = set(n)
    if S_set != n_set:
        continue

    if len(S) == len(n):
        diffs = []
        for i in range(len(S)):
            if S[i] != n[i]:
                diffs.append(i)

        if len(diffs) != 2:
            continue
        n[diffs[0]], n[diffs[1]] = n[diffs[1]], n[diffs[0]]
        if list(S) == n:
            ans += 1

    elif abs(len(S) - len(n)) == 1:
        tmp_S = S[:]
        for i in range(max(len(S), len(n))):
            if S[i] != n[i]:
                if len(S) < len(n):
                    tmp_S.insert(i, n[i])
                else:
                    n.insert(i, S[i])
                break
        
        if tmp_S == n:
            ans += 1


print(ans)