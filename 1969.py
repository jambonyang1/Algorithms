import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DNAs = [[] for _ in range(M)]
for _ in range(N):
    inp = input()
    for i in range(M):
        DNAs[i].append(inp[i])


ans_dna = ''
ans_num = 0
for DNA in DNAs:
    record = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    for x in DNA:
        record[x] += 1
    
    record = sorted(record.items(), key=lambda x: x[1], reverse=True)
    ans_dna += record[0][0]
    ans_num += N - record[0][1]

print(ans_dna)
print(ans_num)