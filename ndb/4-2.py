N = int(input())
answer = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in f'{h}{m}{s}':
                answer += 1

print(answer)










# N += 1
# answer = 0
# if N >= 23:
#     answer += 3600 * 3
#     N -= 3
# elif N >= 13:
#     answer += 3600 * 2
#     N -= 2
# elif N >= 3:
#     answer += 3600
#     N -= 1

# answer += N * 1575

# print(answer, N)