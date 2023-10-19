N, M = map(int, input().split())
pages = list(map(int, input().split()))
d = [] # 잃어버린 페이지 번호들의 배열

for i in range(1, N+1):
    if i not in pages:
        d.append(i)

last = 0 # 가장 최근 목격한 잃어버린 페이지 번호
result = 0 # 사용한 잉크
for i in d: 
    if last: 
        result += min(7, (i - last)*2) # 완전히 새롭게 인쇄하는 것, 이전 페이지에 이어서 연속적으로 인쇄하는 것 중 잉크를 더 적게 사용하는 경우를 선택
    else: # 최근 목격한 페이지 번호가 없을때
        result += 7 # 완전히 새롭게 인쇄해야 함
    last = i

print(result)