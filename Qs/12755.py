N = int(input())
tmp = N
digit = 1

while True:
    a = digit * 9 * (10 ** (digit - 1))
    if tmp > a:
        tmp -= a
        digit += 1
    else:
        break

num = 10 ** (digit-1) + int((tmp-1) / digit)
print(str(num)[(tmp-1) % digit])