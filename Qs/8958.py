import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ques = input()
    state = 0
    ans = 0
    for q in ques:
        if q == 'O':
            state += 1
            ans += state
        else:
            state = 0
    print(ans)