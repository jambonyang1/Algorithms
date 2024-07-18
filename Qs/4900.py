import sys
input = sys.stdin.readline

codes = ['063', '010', '093', '079', '106', '103', '119', '011', '127', '107']
def codetoint(x: str):
    for i in range(10):
        if codes[i] == x:
            return i

def rawtoint(raw: str):
    ret = 0
    digit = len(raw) // 3
    for i in range(digit):
        code = raw[3*i:3*i+3]
        ret += 10 ** (digit - i - 1) * codetoint(code)
    return ret

def inttoraw(x: int):
    ret = ''
    x = str(x)
    for i in x:
        ret = ''.join([ret, codes[int(i)]])
    return ret

while True:
    raw = input().strip()
    if raw == 'BYE':
        break
    nums = list(raw.split('+'))

    A = rawtoint(nums[0])
    B = rawtoint(nums[1])
    print(''.join([raw, inttoraw(A+B)]))