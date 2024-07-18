import sys
input = sys.stdin.readline

N = int(input())
table = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

stds = [list(map(int, input().split())) for _ in range(N ** 2)]

def locate(std, friends):
    result = [0,0]
    fr = 0
    em = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] != 0:
                continue
            tmp_fr = 0
            tmp_em = 0
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if not(0 <= ni < N) or not(0 <= nj < N):
                    continue
                if table[ni][nj] == 0:
                    tmp_em += 1
                elif table[ni][nj] in friends:
                    tmp_fr += 1
            
            if tmp_fr > fr or (tmp_fr == fr and tmp_em > em):
                fr = tmp_fr
                em = tmp_em
                result = [i, j]
    table[result[0]][result[1]] = std
    
for std in stds:
    locate(std[0], std[1:])
stds.sort()
answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        std = table[i][j]
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if not(0 <= ni < N) or not(0 <= nj < N):
                continue
            if table[ni][nj] in stds[std-1][1:]:
                cnt += 1
        
        answer += int((10 ** (cnt-1)) // 1)

print(answer)