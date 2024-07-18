S = input()

alpha = ''
num = ''
for i in S:
    if i.isalpha():
        alpha += i
    else:
        num += i
print(''.join(sorted(alpha)) + ''.join(sorted(num)))