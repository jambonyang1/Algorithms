n = int(input())

# 다이나믹 프로그래밍
# python3 로는 통과안되니 pypy3로 해야 함
dp = [0, 1]
for i in range(2, n+1):
    ans = 4
    for j in range(1, int(i ** (1/2))+1):
        ans = min(ans, dp[i - j ** 2])
    dp.append(ans + 1)

print(dp[-1])


# 브루트 포스
def ran(x):
    upper = int(x ** (1/2))
    return range(1, upper + 1)

def check_square(x):
    return int(x ** (1/2)) == x ** (1/2)

def dyna(x):
    if check_square(x):
        return 1
    
    for i in ran(x):
        if check_square(x - i ** 2):
            return 2
        
    for i in ran(x):
        for j in ran(x - i ** 2):
            if check_square(x - i ** 2 - j ** 2):
                return 3
            
    return 4

print(dyna(n))