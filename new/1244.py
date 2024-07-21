import sys

input = sys.stdin.readline

N = int(input())
switches = list(input().split())
num = int(input())
trials = [list(map(int, input().split())) for _ in range(num)]


def switch(x: int):
    if x == "1":
        return "0"
    else:
        return "1"


for tr in trials:
    g, x = tr
    if g == 1:
        now = x
        while True:
            if now > N:
                break
            switches[now - 1] = switch(switches[now - 1])
            now += x
    else:
        switches[x - 1] = switch(switches[x - 1])
        now = 1
        while True:
            if x - now < 1 or x + now > N:
                break
            if switches[x - now - 1] != switches[x + now - 1]:
                break
            switches[x - now - 1] = switch(switches[x - now - 1])
            switches[x + now - 1] = switch(switches[x + now - 1])
            now += 1

for i in range(N // 20 + 1):
    print(" ".join(switches[i * 20 : min(i * 20 + 20, N)]))
