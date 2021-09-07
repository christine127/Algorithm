##구현: 시뮬레이션과 완전 탐색
#머릿 속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

# 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제

#방향벡터가 자주 사용됨
# 동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#현재 위치
x,y =2,2
for i in range(4):
  #다음 위치
  nx = x +dx[i]
  ny = y+ dy[i]
  print(nx,ny)


## 문제 
#1. 상하좌우
#직접 풀어보기
N = int(input())
D = list(input().split())

x,y = 1,1
for d in D:  
  if (d =='R') &(y<N):
    y += 1
  elif (d == 'L') &(y>1):
    y -= 1
  elif (d == 'U')&(x>1):
    x -= 1
  elif (d == 'D')&(x<N):
    x += 1

print(x,y)

#답안
n = int(input())
x, y = 1,1
plans = input().split()

# L,R,U,D 에 따른 방향
dx = [0,0,-1,-1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
#이동 계획을 하나씩 확인하기
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x+dx[i]
      ny = y+dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny<1 or nx>n or ny> n:
    continue
  x ,y = nx, ny

print(x,y)

#2. 시각
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

n = int(input())

t = 0

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) or '3' in str(j) or '3' in str(k):
        t +=1

print(t)

#3. 왕실의 나이트
c,r = input()
c =ord(c)-96
r = int(r)
count = 0
dc = [-2,-2,2,2,-1,-1,1,1]
dr = [-1,1,-1,1,-2,2,-2,2]

for i in range(8):
  nc = c + dc[i]
  nr = r + dr[i]
  if nc<1 or nr<1 or nc>8 or nr>8:
    continue
  count += 1

print(count)