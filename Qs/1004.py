T = int(input())

for _ in range(T):
    startdest = [int(x) for x in input().split()]
    start = [startdest[0], startdest[1]]
    dest = [startdest[2], startdest[3]]
    circles = []
    count = 0
    N = int(input())
    for _ in range(N):
        circle = [int(x) for x in input().split()]
        startin = False
        destin = False
        if (start[0] - circle[0]) ** 2 + (start[1] - circle[1]) ** 2 < circle[2] ** 2:
            startin = True
        if (dest[0] - circle[0]) ** 2 + (dest[1] - circle[1]) ** 2 < circle[2] ** 2:
            destin = True
        if startin != destin:
            count += 1
    print(count)
