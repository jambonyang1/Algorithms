from itertools import permutations

T = int(input())

for _ in range(T):
    S = list(input())
    isBreak = False
    # next permutation
    # https://hillier.tistory.com/102 참조
    for i in reversed(range(len(S)-1)):
        if S[i] < S[i+1]:
            for j in reversed(range(i+1, len(S))):
                if S[i] < S[j]:
                    S[i], S[j] = S[j], S[i]
                    S = S[:i+1] + S[i+1:][::-1]
                    isBreak = True
                    break
        if isBreak:
            break
    print(''.join(S))


    # 시간 초과 걸린 코드
    # words = list(set(permutations(sorted(S))))

    # for i in range(len(words)):
    #     if list(words[i]) == list(S):
    #         if i == len(words) - 1:
    #             print(S)
    #         else:
    #             print(''.join(words[i+1]))
    #             break