N = int(input())
ns = list(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

ns.sort()

def binary_search(target):
    start = 0
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        if ns[mid] == target:
            return 1
        elif ns[mid] > target:
            end = mid - 1
        elif ns[mid] < target:
            start = mid + 1
    
    return 0
for m in ms:
    print(binary_search(m))