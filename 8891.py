import sys
input = sys.stdin.readline

def posToNum(x, y):
    ret = x * (x+1) // 2
    for i in range(x, x+y-1):
        ret += i

    return ret

def numToPos(a):
    state = 1
    i = 1
    while True:
        if a < state:
            break
        else:
            state += i
            i += 1
    x = i - state + a
    y = i - x
    return x, y

T = int(input())
for _ in range(T):
    a1, a2 = map(int, input().split())
    x1, y1 = numToPos(a1)
    x2, y2 = numToPos(a2)
    print(posToNum(x1+x2, y1+y2))