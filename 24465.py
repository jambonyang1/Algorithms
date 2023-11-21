import sys
input = sys.stdin.readline

stars = [
    [[1, 20], [2, 18]],
    [[2, 19], [3, 20]],
    [[3, 21], [4, 19]],
    [[4, 20], [5, 20]],
    [[5, 21], [6, 21]],
    [[6, 22], [7, 22]],
    [[7, 23], [8, 22]],
    [[8, 23], [9, 22]],
    [[9, 23], [10, 22]],
    [[10, 23], [11, 22]],
    [[11, 23], [12, 21]],
    [[12, 22], [1, 19]],
]

members = []
for _ in range(7):
    m, d = map(int, input().split())
    for star in stars:
        if (m == star[0][0] and d >= star[0][1]) or (m == star[1][0] and d <= star[1][1]):
            members.append(star)
            break

N = int(input())
passes = []
for _ in range(N):
    m, d = map(int, input().split())
    passed = True
    for star in members:
        if (m == star[0][0] and d >= star[0][1]) or (m == star[1][0] and d <= star[1][1]):
            passed = False
            break
    if passed:
        passes.append([m,d])

passes.sort(key = lambda x: (x[0], x[1]))
for p in passes:
    print(p[0], p[1])
if len(passes) == 0:
    print("ALL FAILED")