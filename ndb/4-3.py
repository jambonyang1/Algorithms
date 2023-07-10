loc = input()
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col, row = 0, int(loc[1])

for i in range(0, 8):
    if loc[0] == cols[i]:
        col = i + 1

cases = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
answer = 0
for case in cases:
    ncol = col + case[0]
    nrow = row + case[1]

    if ncol < 1 or ncol > 8 or nrow < 1 or nrow > 8:
        continue

    answer += 1

print(answer)