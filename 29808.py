S = int(input())

num = 0
answers = []
KE = [508, 108]
MS = [212, 305]

if S % 4763 == 0:
    if S == 0:
        num += 1
        answers.append([0,0])
    else:
        S = S // 4763
        for ke in KE:
            for ms in MS:
                for i in range(1, min(S // ke + 1, 201)):
                    if (S - ke * i) % ms == 0 and (S - ke * i) // ms <=200 and i <= 200:
                        num += 1
                        answers.append([i, (S - ke * i) // ms])
        
        
        answers = sorted(answers,key=lambda l:l[1])
        answers = sorted(answers,key=lambda l:l[0])
print(num)
for answer in answers:
    print(answer[0], answer[1])