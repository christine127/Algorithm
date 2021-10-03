#DFS(Depth-First Search): 깊이 우선 탐색
#스택 자료구조(혹은 재귀함수)를 이용

#1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
#2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다. 
#3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다. 

def dfs(graph,v,visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)


graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*9

dfs(graph,1,visited)

#BFS(Breadth-First Search): 너비 우선 탐색 
# 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조 이용

#1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
#2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리합니다.
#3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

from collections import deque

def bfs(graph, start, visited):
  #큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기 
    v = queue.popleft()
    print(v, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

bfs(graph,1, visited) 

## 음료수 얼려 먹기
# 특정 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
# 2. 방문한 지점에서 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
# 3. 모든 노드에 대하여 1~2번 과정을 반복하여, 방문하지 앟은 지점의 수를 카운트합니다.

#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x>=  n or y <= -1 or y >= m:
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] ==0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우 위치들도 모두 재귀적으로 호출- 방문처리 하기 위함
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

# N,M을 공백 기준으로 구분하여 입력 받기
n , m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기 
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)



## 미로탈출
n, m = map(int,input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

from collections import deque

def bfs(x,y):
  # 큐
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    # 현재 위치에서 4가지 방향으로의 위치확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경웅만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  return graph[n-1][m-1]

  # 이동할 네 가지 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))


