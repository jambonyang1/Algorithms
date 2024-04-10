from itertools import combinations
N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            houses.append([i, j])
        if tmp[j] == 2:
            chickens.append([i, j])

distances = dict()
for i in range(len(chickens)):
    distance = []
    for j in range(len(houses)):
        distance.append(abs(chickens[i][0]-houses[j][0]) + abs(chickens[i][1]-houses[j][1]))
    distances[i] = distance

answer = 1e9
for case in list(combinations(range(len(chickens)), M)):
    num_h = len(houses)
    tmp = [1e9 for _ in range(num_h)]
    for ch in case:
        for i in range(num_h):
            tmp[i] = min(tmp[i], distances[ch][i])
    answer = min(answer, sum(tmp))

print(answer)