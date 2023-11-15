N = int(input())
arr = list(map(int, input().split()))

high = 1
high_state = 1
low = 1
low_state = 1
for i in range(1, N):
    if arr[i] >= arr[i-1]:
        high_state += 1
    else:
        high = max(high, high_state)
        high_state = 1

    if arr[i] <= arr[i-1]:
        low_state += 1
    else:
        low = max(low, low_state)
        low_state = 1
high = max(high, high_state)
low = max(low, low_state)

print(max(high, low))