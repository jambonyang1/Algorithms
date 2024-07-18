import sys
input = sys.stdin.readline

fibo = [1, 2, 4]
for i in range(3, 11):
    fibo.append(fibo[i-1]+fibo[i-2]+fibo[i-3])

T = int(input())
for _ in range(T):
    n = int(input())
    print(fibo[n-1])