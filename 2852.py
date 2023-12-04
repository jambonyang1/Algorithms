N = int(input())
scores = {
    '1': 0,
    '2': 0
}
times = {
    '1': 0,
    '2': 0
}
recent = 0
for _ in range(N):
    team, time = input().split()
    h, m  = map(int, time.split(':'))
    time = h * 60 + m
    if scores['1'] < scores['2']:
        times['2'] += time - recent
    elif scores['1'] > scores['2']:
        times['1'] += time - recent
    scores[team] += 1
    recent = time

if scores['1'] < scores['2']:
        times['2'] += 48 * 60 - recent
elif scores['1'] > scores['2']:
    times['1'] += 48 * 60 - recent

print('{:02d}:{:02d}'.format(times['1']//60, times['1']%60))
print('{:02d}:{:02d}'.format(times['2']//60, times['2']%60))