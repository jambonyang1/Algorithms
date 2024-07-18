K = int(input())
bds = list(map(int, input().split()))

answer = [list() for _ in range(K)]

def recursive(li, level, i):
    answer[level].append(li[i])
    if len(li) == 1:
        return
    recursive(li[:i], level+1, i//2)
    recursive(li[i+1:], level+1, i//2)

recursive(bds, 0, len(bds)//2)

for li in answer:
    print(*li)