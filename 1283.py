N = int(input())

shortcuts = list()

def find(li):
    for i in range(len(li)):
        tmp = li[i][0].lower()
        if tmp not in shortcuts:
            shortcuts.append(tmp)
            return True, [i, 0]
    
    for i in range(len(li)):
        for j in range(1, len(li[i])):
            tmp = li[i][j].lower()
            if tmp not in shortcuts:
                shortcuts.append(tmp)
                return True, [i, j]
    
    return False, []

for _ in range(N):
    li = list(input().split())
    result, index = find(li)
    if result:
        i, j = index[0], index[1]
        li[i] = li[i][:j] + "[" + li[i][j] + "]" + li[i][j+1:] 
        print(' '.join(li))
    else:
        print(' '.join(li))
