#그리디 알고리즘(탐욕법): 현재상황에서 지금 당장 좋은 것만 고르는 방법
#단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적해를 구할 수 있는지 검토가 필요함
#코딩테스트에서 대부분의 그리드 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 경우가 많음. 

##예제 - 거스름돈
n = 1260
count = 0

array = [500,100,50,10]
for coin in array: 
  count += n //coin
  n %=coin #나눈 뒤 나머지의 수

print(count)

##문제1 -1이 될 때까지
n , k = map(int, input().split())
result = 0 
while True:
  #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n//k) *k
  result += (n -target)
  n = target
  #N이 K보다 작을 때 반복문 탈출
  if n < k :
    break
  #K로 나누기
  result += 1
  n //= k 

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)


##문제2 - 곱하기 혹은 더하기
num_list = list(map(int,list(input())))
result = num_list[0] 

for num in num_list[1:]:
  if (num <=1) or (result <=1) :
    result += num
  else:
    result *= num

print(result)

##문제3 - 모험가 길드
n = int(input())
data = list(map(int,input.split()))
data.sort()

result = 0
count = 0
for i in data:
  count += 1
  if count >= i:
    result +=1
    count = 0

print(result)