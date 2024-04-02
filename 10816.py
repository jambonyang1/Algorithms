N = int(input())
ns = list(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

ns.sort()

def binary_search(target):
    left = 0
    right = len(ns) - 1
    first_occurrence = -1
    last_occurrence = -1

    # 첫 번째 출현 위치 찾기
    while left <= right:
        mid = (left + right) // 2
        if ns[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif ns[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # 만약 목표값이 리스트 안에 없으면 0 반환
    if first_occurrence == -1:
        return 0

    # 마지막 출현 위치 찾기
    left = 0
    right = len(ns) - 1
    while left <= right:
        mid = (left + right) // 2
        if ns[mid] == target:
            last_occurrence = mid
            left = mid + 1
        elif ns[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_occurrence - first_occurrence + 1

answers = []
for m in ms:
    answers.append(str(binary_search(m)))

print(' '.join(answers))