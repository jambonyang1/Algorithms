word = input()
word = word.upper()
li = list(word)
se = set(li)

most = []
most_num = 0
for w in se:
    cnt = li.count(w)
    if cnt > most_num:
        most = [w]
        most_num = cnt
    elif cnt == most_num:
        most.append(w)

if len(most) > 1:
    print('?')
else:
    print(most[0])