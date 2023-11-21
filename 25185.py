T = int(input())
for _ in range(T):
    rest = False
    cards = list(input().split())
    cards.sort()

    tmp = sorted(list(set(cards)), key= lambda x: (x[1], x[0]))
    if len(tmp) > 2:
        for i in range(len(tmp)-2):
            num, sym = tmp[i][0], tmp[i][1]
            for j in range(1, 3):
                if int(tmp[i+j][0]) != int(num) + j or tmp[i+j][1] != sym:
                    break
                if j == 2:
                    rest = True
    else:
        rest = True
    
    if rest:
        print(":)")
    else:
        print(":(")