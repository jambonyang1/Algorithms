N = input().split()
p = int(N[0])
q = int(N[1])
divs = []
for i in range(1, p + 1):
    if p % i == 0:
        divs.append(i)

if q > len(divs):
    print(0)
else:
    print(divs[q-1])