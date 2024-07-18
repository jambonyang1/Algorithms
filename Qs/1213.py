s = input()
d = dict()
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

odd_count = 0
odd = ''
for key in d:
    if d[key] % 2 == 1:
        odd_count += 1
        odd = key
        d[key] -= 1
ans = ''
if odd_count > 1:
    ans = 'I\'m Sorry Hansoo'
else:
    d = dict(sorted(d.items()))
    part = ''
    for key in d:
        part += (d[key] // 2) * key
    ans = part + odd + part[::-1]

print(ans)