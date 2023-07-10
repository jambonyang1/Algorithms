N = int(input())

fihun = N // 500
N = N % 500
onehun = N // 100
N = N % 100
fifty = N // 50
N = N % 50
ten = N // 10

print(fihun, onehun, fifty, ten)