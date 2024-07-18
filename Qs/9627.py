N = int(input())

one = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
eleven = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def num(x):
    if 1<= x <= 10:
        return one[x-1]
    elif 11 <= x < 20:
        return eleven[x-11]
    elif 20 <= x < 100:
        t, o = x // 10, x % 10
        if o != 0:
            return twenty[t - 2] + one[o-1]
        else:
            return twenty[t - 2]
    else:
        h, t = x // 100, x % 100
        if t != 0:
            return one[h-1] + 'hundred' + num(t)
        else:
            return one[h-1] + 'hundred'

words = []
length = 0
for _ in range(N):
    word = input()
    words.append(word)
    if word != '$':
        length += len(word)

ans = length
while True:
    if ans == length + len(num(ans)):
        break
    ans += 1

for i in range(N):
    if words[i] == '$':
        words[i] = num(ans)
        break

print(' '.join(words))