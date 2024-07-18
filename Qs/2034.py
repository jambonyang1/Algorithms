import sys
input = sys.stdin.readline

scales = {
    9: 'A',
    11: 'B',
    0: 'C',
    2: 'D',
    4: 'E',
    5: 'F',
    7: 'G'
}


n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

ans = []
for i in scales.keys():
    scale = i
    isAns = True
    for step in li:
        scale = (scale + step) % 12
        if scale not in scales:
            isAns = False
            break

    if isAns:
        print(scales[i], scales[scale])