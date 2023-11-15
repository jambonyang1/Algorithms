N = int(input())
A = list(map(int, input().split()))

mom = 1
for i in A:
    mom *= i
son = 0
for i in A:
    son += mom // i

a, b = son, mom
while True:
    if b == 0:
        break
    a, b = b, a % b

print(f'{mom//a}/{son//a}')