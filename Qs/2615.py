table = [list(map(int, input().split())) for _ in range(19)]

result = 0

def find(color):
    # 가로
    for i in range(19):
        tmp = 0
        for j in range(19):
            if table[i][j] == color:
                tmp += 1
            else:
                if tmp == 5:
                    return True, [i, j-5]
                tmp = 0
        if tmp == 5:
            return True, [i, 10]

    #세로
    for i in range(19):
        tmp = 0
        for j in range(19):
            if table[j][i] == color:
                tmp += 1
            else:
                if tmp == 5:
                    return True, [j-5, i]
                tmp = 0
        if tmp == 5:
            return True, [10, i]
    
    # 대각선 밑 부분
    for i in range(19):
        tmp = 0
        for j in range(19-i):
            if table[i+j][j] == color:
                tmp += 1
            else:
                if tmp == 5:
                    return True, [i+j-5, j-5]
                tmp = 0
        if tmp == 5:
            return True, [10, 10-i]
    # 대각선 윗 부분
    for i in range(19):
        tmp = 0
        for j in range(19-i):
            if table[j][i+j] == color:
                tmp += 1
            else:
                if tmp == 5:
                    return True, [j-5, i+j-5]
                tmp = 0
        if tmp == 5:
            return True, [10-i, 10]
    
    return False, [-1, -1]

no = True
for i in [1, 2]:
    tf, loc = find(i)
    if tf:
        print(i)
        print(loc[0]+1, loc[1]+1)
        no = False
        break

if no:
    print(0)