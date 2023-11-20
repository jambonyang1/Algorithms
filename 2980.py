import sys
input = sys.stdin.readline

time = 0
loc = 0
N, L = map(int, input().split())
for _ in range(N):
    D, R, G = map(int, input().split())
    time += D - loc
    left = time % (R + G)
    if left < R:
        time += R - left
    loc = D

time += L - loc
print(time)