a, b = map(int, input().split())

if b > a:
    a, b = b, a

def euclid(max, min):
    while True:
        r = max % min
        if r == 0:
            break
        max = min
        min = r
    return min

GCD = euclid(a,b)
LCM = int(a * b / GCD)

print(GCD)
print(LCM)