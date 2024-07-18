N, M = map(int, input().split())
woods = list(map(int, input().split()))

def binary_search():
    left = 0
    right = max(woods)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for w in woods:
            cnt += max(w, mid) - mid
        
        if cnt >= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(binary_search())