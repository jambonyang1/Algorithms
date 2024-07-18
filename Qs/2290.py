s, li = input().split()
s = int(s)
li = list(map(int, list(li)))

rules = [
    ['full', 'empty', 'full', 'full', 'empty', 'full', 'full', 'full', 'full', 'full'],
    ['both', 'right', 'right', 'right', 'both', 'left', 'left', 'right', 'both', 'both'],
    ['empty', 'empty', 'full', 'full', 'full', 'full', 'full', 'empty', 'full', 'full'],
    ['both', 'right', 'left', 'right', 'right', 'right', 'both', 'right', 'both', 'right',],
    ['full', 'empty', 'full', 'full', 'empty', 'full', 'full', 'empty', 'full', 'full']
]

ans = ['' for _ in range(2*s + 3)]

def floor(code):
    ret = ''
    if code == 'empty':
        ret = ' ' * (s+2)
    else:
        ret =  ' ' + '-' * s + ' '
    
    return ret + ' '

def side(code):
    ret = ' '
    if code == 'left':
        ret = '|' + ' ' * (s+1)
    elif code == 'right':
        ret = ' ' * (s+1) + '|'
    else:
        ret = '|' + ' ' * s + '|'
    
    return ret + ' '

for i in range(5):
    if i % 2 == 1:
        tmp = ''
        for x in li:
            tmp += side(rules[i][x])
        for _ in range(s):
            print(tmp)

    else:
        tmp = ''
        for x in li:
            tmp += floor(rules[i][x])
        print(tmp)