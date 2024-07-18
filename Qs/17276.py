import sys
input = sys.stdin.readline

T = int(input())

def rotate(table, n, d):
    d = (d // 45) % 8
    for j in  range(d):
        for i in range(1, n//2+1):
            table[n//2-i][n//2-i], table[n//2-i][n//2], table[n//2-i][n//2+i], table[n//2][n//2+i], table[n//2+i][n//2+i], table[n//2+i][n//2], table[n//2+i][n//2-i], table[n//2][n//2-i] = table[n//2][n//2-i], table[n//2-i][n//2-i], table[n//2-i][n//2], table[n//2-i][n//2+i], table[n//2][n//2+i], table[n//2+i][n//2+i], table[n//2+i][n//2], table[n//2+i][n//2-i]

    return table


for _ in range(T):
    n, d = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    for line in rotate(table, n, d):
        print(' '.join(map(str, line)))