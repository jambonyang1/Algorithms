import sys
input = sys.stdin.readline

N, M = map(int,input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ans = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        ans += 1
    else:
        isClear = True
        for i in range(4):
            new_r = r+dy[(d-i)%4]
            new_c = c+dx[(d-i)%4]
            if 0 <= new_r < N and 0 <= new_c < M:
                if room[new_r][new_c] == 0:
                    isClear = False
                    break
        
        if isClear:
            new_r = r-dy[d]
            new_c = c-dx[d]
            if 0 <= new_r < N and 0 <= new_c < M:
                if room[new_r][new_c] == 1:
                    break
                else:
                    r = new_r
                    c = new_c
            else: break
        else:
            for i in range(4):
                d = (d-1)%4
                new_r = r+dy[d]
                new_c = c+dx[d]
                if 0 <= new_r < N and 0 <= new_c < M:
                    if room[new_r][new_c] == 0:
                        r = new_r
                        c = new_c
                        break
    
print(ans)