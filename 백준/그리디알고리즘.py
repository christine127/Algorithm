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