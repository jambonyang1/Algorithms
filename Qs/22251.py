N, K, P, X = map(int, input().split())

leds = {
    0: '1110111',
    1: '0010010',
    2: '1011101',
    3: '1011011',
    4: '0111010',
    5: '1101011',
    6: '1101111',
    7: '1010010',
    8: '1111111',
    9: '1111011' 
}

def find_diff(x: int, y: int):
    ret = 0
    for i in range(7):
        if leds[x][i] != leds[y][i]:
            ret += 1
    return ret

ans = 0
X = str(X).zfill(K)
for i in range(1, N+1):
    i = str(i).zfill(K)

    sum_diff = 0
    for j in range(K):
        sum_diff += find_diff(int(i[j]), int(X[j]))
    
    if 0 < sum_diff <= P:
        ans += 1

print(ans)