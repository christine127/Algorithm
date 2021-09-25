# 탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# DFS/BFS: 대표적인 그래프 탐색 알고리즘

# 자료구조
# 스택 자료구조(first in last out)
# 입구와 출구가 동일한 형태 예) 박스 쌓기

 # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

#큐 자료구조(first in first out)
#입구와 출구가 모두 뚫려 있는 터널 형태

 # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()

# 큐(Queue) 구현을 위해 deque 라이브러리 사용(리스트는 시간 복잡도가 올라감)
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft() 

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력


