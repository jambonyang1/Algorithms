from itertools import combinations

smalls = []
for _ in range(9):
    smalls.append(int(input()))

for comb in list(combinations(smalls, 7)):
    if sum(comb) == 100:
        comb = list(comb)
        comb.sort()
        for i in comb:
            print(i)
        break