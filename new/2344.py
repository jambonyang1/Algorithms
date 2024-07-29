import sys

input = sys.stdin.readline
N, M = map(int, input().split())
mirrors = [list(map(int, input().split())) for _ in range(N)]


def next_direction(dr, dc, isMirror):
    if isMirror == 0:
        return dr, dc

    if dr == 0:
        if dc == 1:
            return -1, 0
        else:
            return 1, 0
    elif dr == -1:
        return 0, 1
    else:  # dr == 1
        return 0, -1


def locToNum(r, c, dr, dc):
    if dr == 0 and dc == -1:
        return r + 1
    elif dr == 1 and dc == 0:
        return N + c + 1
    elif dr == 0 and dc == 1:
        return 2 * N + M - r
    else:
        return 2 * N + 2 * M - c


ans = []
for i in range(N):
    dr, dc = 0, 1
    r, c = i, 0
    while True:
        dr, dc = next_direction(dr, dc, mirrors[r][c])
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N) or not (0 <= nc < M):
            break
        r, c = nr, nc
    ans.append(locToNum(r, c, dr, dc))

for i in range(M):
    dr, dc = -1, 0
    r, c = N - 1, i
    while True:
        dr, dc = next_direction(dr, dc, mirrors[r][c])
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N) or not (0 <= nc < M):
            break
        r, c = nr, nc
    ans.append(locToNum(r, c, dr, dc))

for i in range(N):
    dr, dc = 0, -1
    r, c = N - i - 1, M - 1
    while True:
        dr, dc = next_direction(dr, dc, mirrors[r][c])
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N) or not (0 <= nc < M):
            break
        r, c = nr, nc
    ans.append(locToNum(r, c, dr, dc))

for i in range(M):
    dr, dc = 1, 0
    r, c = 0, M - i - 1
    while True:
        dr, dc = next_direction(dr, dc, mirrors[r][c])
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N) or not (0 <= nc < M):
            break
        r, c = nr, nc
    ans.append(locToNum(r, c, dr, dc))

print(" ".join(map(str, ans)))
