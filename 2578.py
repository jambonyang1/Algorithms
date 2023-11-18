table = []
for _ in range(5):
    table.append(list(map(int, input().split())))

calls = []
for i in range(5):
    calls.append(list(map(int, input().split())))

horizontal = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

vertical = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

diagonal = {
    0: 0,
    1: 0,
}

def check_bingo():
    cnt = 0
    for i in range(5):
        if horizontal[i] == 5:
            cnt += 1
        if vertical[i] == 5:
            cnt += 1
        if i < 2:
            if diagonal[i] == 5:
                cnt += 1
        if cnt >= 3:
            return True
    return False

cnt = 0
for call in calls:
    for c in call:
        cnt += 1
        for i in range(5):
            for j in range(5):
                if c == table[i][j]:
                    horizontal[i] += 1
                    vertical[j] += 1
                    if i == j:
                        diagonal[0] += 1
                    if i+j == 4:
                        diagonal[1] += 1
        if check_bingo():
            print(cnt)
            break
    if check_bingo():
        break
        