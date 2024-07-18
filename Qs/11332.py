from math import factorial
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S, N, T, L = input().split()
    N, T, L = map(int, [N, T, L])
    L = 1e8 * L / T
    if S == 'O(N^2)':
        for _ in range(2):
            L /= N
            if L < 1:
                print('TLE!')
                break
        
    elif S == 'O(N^3)':
        for _ in range(3):
            L /= N
            if L < 1:
                print('TLE!')
                break
    elif S == 'O(2^N)':
        for _ in range(N):
            L /= 2
            if L < 1:
                print('TLE!')
                break
    elif S == 'O(N!)':
        for i in range(N, 0, -1):
            L /= i
            if L < 1:
                print('TLE!')
                break
 
    if L >= 1:
        print('May Pass.')