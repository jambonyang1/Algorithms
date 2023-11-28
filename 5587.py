n = int(input())
cards = [[], [i for i in range(1, 2*n+1)]]
scores = [0, 0]
for _ in range(n):
    x = int(input())
    cards[0].append(x)
    cards[1].remove(x)
cards[0].sort()

top = 0
now = 0
while True:
    new = 0
    for i in cards[now]:
        if i > top:
            new = i
            cards[now].remove(i)
            break
    top = new
    if len(cards[now]) == 0:
        scores[now] = len(cards[now - 1])
        scores[now-1] = 0
        break
    
    now = (now + 1) % 2

print(scores[0])
print(scores[1])