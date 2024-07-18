old = input()
new = input()
old_colors = {'R': 0, 'G': 0, 'B': 0, 'Y': 0, '*': 0}
new_colors = {'R': 0, 'G': 0, 'B': 0, 'Y': 0, '*': 0}
for i in old:
    old_colors[i] += 1
for i in new:
    new_colors[i] += 1
count = 0
for key in old_colors.keys():
    count += abs(old_colors[key] - new_colors[key])
print(int(count/2))