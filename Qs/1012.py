# 시도 3
# 스택을 이용한 dfs

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_stack(start_x, start_y):
    stack = [(start_x, start_y)] # 시작 타일을 스택에 넣어둔 채로 시작
    graph[start_y][start_x] = 0
    while stack: # 스택에 요소가 남아있는 한 계속 루프 돌도록
        x, y = stack.pop() # (x, y) 라는 타일을 방문 후 스택에서 pop
        for i in range(4): # 상하좌우 4방향을 전부 거침
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N: # 인접 타일이 그래프를 넘어가지 않는지 확인
                continue
            if graph[ny][nx] == 1: # 인접 타일에 배추가 있을 경우 스택에 해당 타일을 추가
                stack.append((nx, ny))
                graph[ny][nx] = 0  # 해당 타일을 방문했으니 그래프에서 값을 0으로 변경


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    targets = [] # 배추가 있는 타일의 위치를 저장하는 list
    answer = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        targets.append((y,x)) 
    
    for target in targets: # targets 내 타일 이외엔 전부 0이므로 굳이 거칠 필요 없음
        y, x = target
        if graph[y][x] == 1: # 입력할 땐 target 타일의 값이 1이지만 dfs를 거치면서 0으로 변할 수 있음. 따라서 방문하지 않은 타일만 dfs로 탐색하기 위해 해당 조건문을 달아줌
            dfs_stack(x, y)
            answer += 1
    print(answer)




# answer = []
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     graph = [[0] * M for _ in range(N)]
#     targets = []
#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[y][x] = 1
#         targets.append((y,x))
    
#     tmp = 0
#     for target in targets:
#         y, x = target
#         if graph[y][x] == 1:
#             dfs_stack(x, y)
#             tmp += 1
#     answer.append(tmp)

# for i in answer:
#     print(i)

# 시도 1
# 12% 까지는 정답이 나오지만, 그 이후로는 런타임 에러가 뜬다.
# 예상 원인은 DFS로 인한 너무 깊은 재귀로 추정됨 --> 재귀를 사용하지 않아도 되는 BFS나 스택으로 구현한 DFS 로 해결

# def dfs(x, y):
#     if x < 0 or x >= M or y < 0 or y >= N: # 그래프를 벗어날 경우 False를 반환
#         return False
#     if graph[y][x] == 1: # 배추가 있는 타일일 경우
#         graph[y][x] = 0 # 0으로 타일값을 변경해 방문한 타일이라는 것을 표시
#         # 현재 점유하고 있는 타일의 상하좌우 방향으로 다시 DFS 알고리즘 수행
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True # 이 과정으로 온 경우에만 한 배추의 군집이 있다는 뜻이므로 answer += 1을 할 조건 충족
#     return False

# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     graph = [[0] * M for _ in range(N)]
#     answer = 0
    
#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[y][x] = 1
    
#     for i in range(N):
#         for j in range(M):
#             if dfs(j, i):
#                 answer += 1
#     print(answer)



# 시도 2
# BFS에서도 동일하게 12% 까지는 정답이 나온다. 하지만 시간초과로 실패하게 된다.
# 최대한 시간을 줄여보려고 그래프의 모든 노드를 거치는게 아니라 입력값에서 받은 배추의 위치만 탐색하도록 해도 시간 초과 오류는 해결되지 않음. 최대 2500칸의 작은 맵이기 때문에 큰 영향을 안주는 건 당연한듯
# 13% 째에 일방통행의 긴 노드들의 연결이 있지 않을까 추정됨
# 재귀없는 DFS로 해결해보려고 한다.

# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(i, j):
#     queue = deque()
#     queue.append((i, j)) # 큐에 시작 타일의 위치 정보를 삽입
#     graph[i][j] = 0 # 큐에 타일의 위치 정보를 넣은 다음엔 반드시 방문했다는 표시를 해야 한다.
#     while queue:
#         y,x = queue.popleft()
        
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]

#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue

#             if graph[ny][nx] == 1:
#                 queue.append((ny, nx)) # 큐에 인접 타일의 위치 정보를 삽입
#                 graph[ny][nx] = 0 # (recap)큐에 타일의 위치 정보를 넣은 다음엔 반드시 방문했다는 표시를 해야 한다.

# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     graph = [[0] * M for _ in range(N)]
#     targets = []
#     answer = 0

#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[y][x] = 1
#         targets.append((y,x))
    
#     for target in targets: # 배추가 있는 타일인지
#         i, j = target
#         if graph[i][j] == 1: # 방문하지 않은 타일인지
#             bfs(i,j)
#             answer += 1
            
#     print(answer)