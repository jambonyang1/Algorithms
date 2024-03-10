wheels = [input() for _ in range(4)]
indices = [0, 0, 0, 0]
K = int(input())
for _ in range(K):
    w, d = map(int, input().split())
    rotates = [0, 0, 0, 0]
    rotates[w-1] = d
    # 처음 회전시킨 톱니바퀴로부터 왼쪽 톱니바퀴로 연쇄되는 과정
    for i in reversed(range(1, w)):
        d = -d # 톱니바퀴가 하나씩 진행될때마다 회전되는 방향은 반대가 된다
        j = i-1
        if wheels[i][(indices[i]-2)%8] == wheels[j][(indices[j]+2)%8]: # i 톱니바퀴의 9시방향과 j 톱니바퀴의 3시 방향의 극이 같을 때 회전의 연쇄는 중단된다
            break
        else:
            rotates[j] = d

    d = rotates[w-1] # d는 기존 값으로 다시 리셋
    for i in range(w-1, 3):
        d = -d
        j = i+1
        if wheels[i][(indices[i]+2)%8] == wheels[j][(indices[j]-2)%8]:
            break
        else:
            rotates[j] = d
    
    for i in range(4):
        indices[i] = (indices[i] - rotates[i]) % 8


print(sum([2 ** i if wheels[i][indices[i]] == '1' else 0 for i in range(4)]))