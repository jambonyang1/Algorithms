S = input()
d = []

for i in range(1, len(S) // 2 + 1):
    cursor = 0
    tmp = []
    while cursor <= len(S):
        tmp.append(S[cursor:cursor+i])
        cursor += i
    d.append(tmp)

for case in d:
    cnt = 0
    result = ''
    for i in range(len(case) - 1):
        if case[i] == case[i + 1]:
            cnt += 1
        else:
            if cnt == 0:
                
    tmp = case [0]


