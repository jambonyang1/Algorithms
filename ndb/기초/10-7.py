def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

N, M  = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    uf, a, b = map(int, input().split())
    if uf == 0:
        union(parent, a, b)
    elif uf == 1:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')