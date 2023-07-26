f = [1,1]+ [0] * 98

def fibo(x):
    if f[x] != 0:
        return f[x]
    f[x] = fibo(x-1) + fibo(x-2)
    return f[x]

for i in range(2,len(f)):
    f[i] = f[i-1] + f[i-2]

print(f)