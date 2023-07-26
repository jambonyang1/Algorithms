array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

MAX = len(array)

# 선택정렬 Selection sort
def SelectionSort():
    for i in range(MAX):
        min = i
        for j in range(i + 1, MAX):
            min = j if array[j] < array[min] else min
        array[i], array[min] = array[min], array[i]


# 삽입정렬 Insertion sort
def InsertionSort():
    for i in range(MAX):
        for j in reversed(range(i)):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                break

# 코드 안보고 완전히 내가 구현한 것.
# 새로 tmp라는 list를 만들어야된다는 단점이 있다. 그리고 조금 더 복잡하다.
# tmp = []
# for i in range(MAX):
#     num = array[i]
#     len_tmp = len(tmp)
#     for j in range(len_tmp):
#         if num <= tmp[j]:
#             tmp.insert(j, num)
#             break
#     if len_tmp == len(tmp):
#         tmp.append(num)
# array = tmp

# 퀵정렬 Quick sort
def QuickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return QuickSort(left) + [pivot] + QuickSort(right)

# 계수정렬 Count sort
def CountSort(array):
    count = [0] * (max(array) + 1)
    for i in range(MAX):
        count[array[i]] += 1
    ret = []
    for i in range(MAX):
        ret += [i] * count[i]
    return ret


print(CountSort(array))