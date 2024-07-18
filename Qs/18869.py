import sys
input = sys.stdin.readline

M, N = map(int, input().split())
spaces = [list(map(int, input().split())) for _ in range(M)]

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1

news = []
for space in spaces:
    st_space = sorted(space)
    new = []
    for pn in space:
        new.append(binary_search(st_space, pn))
    news.append(new)

answer = 0
for i in range(M-1):
    for j in range(i+1, M):
        if news[i] == news[j]:
            answer += 1

print(answer)