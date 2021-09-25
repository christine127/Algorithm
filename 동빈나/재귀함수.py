# 재귀함수(Recursive Function): 자기 함수를 다시 호출하는 함수

# 파이썬에서는 재귀 호출하는 깊이 제한이 있으므로 오류가 뜸
def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()

# recursive_function()

##재귀함수 종료조건
  # 종료 조건 명시하지 않으면 함수 무한히 호출하는

def recursive_function(i):
  if i==100:
      return 
  print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
  recursive_function(i+1)
  print(i,'번째 재귀 함수를 종료합니다.')

# recursive_function(1)

## 팩토리얼 구현 예제

#반복적으로 구현한 n!
def factorial_iterative(n):
  #1부터 n까지의 수를 차례대로 곱하기 
  result = 1
  for i in range(1,n+1):
    result *= i
  return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1: #n이 1 이하인 경우 1 반환
    return 1
  # n! = n * (n-1)!을 그대로 코드로 작성하기
  return n*factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))

## 유클리드 호제법
# 두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 할 때, A,B의 최대공약수는 B와 R의 최대공약수와 같다 

def gcd(a,b):
  if a%b ==0:
    return b
  else:
    return gcd(b, a%b)

print(gcd(192,162))

#Tips
# 스택을 사용해야 할 때, 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많음. 
