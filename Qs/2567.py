import sys
input = sys.stdin.readline

N = int(input())

def recur(papers):
    total = 0
    pass
    #for paper in papers:


papers = []



ans = 160
log = []
for _ in range(N):
    l, d = map(int, input().split())
    for paper in papers:
        l_dist = abs(l - paper[0])
        d_dist = abs(d - paper[1])
        if l_dist > 10 or d_dist > 10:
            continue
        ans -= 2 * (10 - l_dist) + 2 * (10 - d_dist)
        log.append([ans, l, d, paper])
        
    papers.append([l, d])
print(log)
print(ans)