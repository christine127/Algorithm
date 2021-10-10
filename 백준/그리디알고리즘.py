# 동전0
N , K = map(int,input().split(' '))
coin = []
for _ in range(N):
  coin.append(int(input()))
useful_coin = list(filter(lambda x: x < K, coin))[::-1]

count = 0
i = 0
remainder = K
while remainder >0:
  count += remainder // useful_coin[i]
  remainder = remainder % useful_coin[i]
  i +=1 

print(count)

#회의실 배정 
N = int(input())
meeting = []
for _ in range(N):
  st, en = map(int, input().split(' '))
  meeting.append((st,en,en-st))#시작, 끝, 회의시간
  
meeting.sort(key = lambda x: (x[0],x[2]))
print(meeting)
# count = []
# for meet in meeting:
#   lst = []
#   lst.append(meet)
#   for another_meet in meeting:
#     if  
#   count.append(len(lst))  
  
# print(max(count))