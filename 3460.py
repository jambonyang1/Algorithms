T = int(input())

for _ in range(T):
    N = int(input())
    i = 0
    ll = list()
    while N != 0:
        if 2**i > N:
            N -= 2**(i-1)
            ll.append(i-1)
            i = 0
        i += 1
    ll.sort()
    print(*ll, sep=' ')