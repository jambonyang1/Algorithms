M, N = map(int, input().split())
Ls = list(map(int, input().split()))
Ls.sort()

def binary_search():
    left = 1
    right = Ls[-1]
    result = 0
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for l in Ls:
            cnt += l // mid
        
        if cnt >= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(binary_search())