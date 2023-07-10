N = int(input())
N += 1
answer = 0
if N >= 23:
    answer += 3600 * 3
    N -= 3
elif N >= 13:
    answer += 3600 * 2
    N -= 2
elif N >= 3:
    answer += 3600
    N -= 1

answer += N * 1575

print(answer, N)