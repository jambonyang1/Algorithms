import sys
input = sys.stdin.readline

T = int(input())

def checkWin(table, mark):
    for i in range(3):
        if table[i] == mark*3:
            return True
    
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i] == mark:
            return True
    
    if table[0][0] == table[1][1] == table[2][2] == mark:
        return True
    
    if table[0][2] == table[1][1] == table[0][2] == mark:
        return True
    
    return False

def test(table, mark):
    for i in range(3):
        for j in range(3):
            if table[i][j] != '-':
                continue
            tmp = table[:]
            tmp[i] = list(tmp[i])
            tmp[i][j] = mark
            tmp[i][j] = ''.join(tmp[i][j])
            if checkWin(tmp, mark):
                return tmp

for i in range(1, T+1):
    table = []
    for _ in range(3):
        table.append(input())
    mark = input()

    result = test(table, mark)
    print(f'Case ${i}:')
    for line in result:
        print(line)

    

