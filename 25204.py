from functools import cmp_to_key
import sys
input = sys.stdin.readline

T = int(input())

def compare(a, b):
    ret = -1 if len(a) <= len(b) else 1

    for i in range(min(len(a), len(b))):
        ai = a[i]
        bi = b[i]
        
        if ai == bi:
            continue
        
        if ai == '-': return 1
        if bi == '-': return -1
        if ai.upper() == bi.upper():
            if ai < bi:
                return -1
            else:
                return 1
        else:
            if ai.upper() < bi.upper():
                return -1
            else:
                return 1

        break
    
    return ret

for _ in range(T):
    N = int(input())
    d = []
    for i in range(N):
        d.append(input())

    d = sorted(d, key=cmp_to_key(compare))
    for i in d:
        print(i, end='')