N = int(input())
tops = input().split()

able = set()

for top in tops:
    if top.endswith('Cheese'):
        able.add(top)

if len(able) >= 4:
    print("yummy")
else:
    print("sad")