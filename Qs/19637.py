import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
names = []
values = []
for _ in range(N):
    name, value = map(int, input().split())
    names.append(name)
    values.append(value)

def binary_search(target):
    left = 0
    right = N-1
    result = 0
    while left <= right:
        mid = (left + right) // 2

        if values[mid] < target:
            left = mid + 1
        elif values[mid] >= target:
            result = mid
            right = mid - 1
    
    return result