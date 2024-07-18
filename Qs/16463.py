N = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False

ans = 0
now = 1
for y in range(2019, N+1):
    leap = isLeap(y)
    for day in days:
        if day == 28 and leap:
            day += 1
        
        if (now + 12) % 7 == 4:
            ans += 1
        
        now = (now + day) % 7

print(ans)