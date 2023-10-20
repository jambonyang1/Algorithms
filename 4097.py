import sys
input = sys.stdin.readline

def fn(array):
    pos = 0
    max_value = min(array)
    for i in array:
        if pos + i >= 0:
            pos += i
            max_value = max(max_value, pos)
        else:
            pos = 0
            max_value = max(max_value, i)

    return max_value

while True:
    T = int(input())
    if not T:
        break
    array = []
    for _ in range(T):
        array.append(int(input()))
    
    print(fn(array))