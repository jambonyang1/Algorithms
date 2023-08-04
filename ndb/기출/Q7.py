N = input()
half = len(N) // 2
answer = [0, 0]
for i in range(half):
    answer[0] += int(N[i])
for i in range(half):
    answer[1] += int(N[i+half])

if answer[0] == answer[1]:
    print("LUCKY")
else:
    print("READY")