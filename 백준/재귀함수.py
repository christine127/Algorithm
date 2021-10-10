#팩토리얼
def factorial(n):
  if n <= 1:
    return 1
  else: 
    return n*factorial(n-1)

print(factorial(int(input())))

#피보나치
def Fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1  
  else:
    return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(int(input())))

#별찍기
def star(n):
  global Map

  if n == 3:
    Map[0][:3] = [1]*3
    Map[1][:3] = [1,0,1]
    Map[2][:3] = [1]*3 
    return

  a = n//3
  star(a)
  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        continue
      for k in range(a):
        Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]

N= int(input())
Map = [[0]*N  for _ in range(N)]
star(N)

for i in Map:
  for j in i:
    if j == 1:
      print('*', end = '')
    else:
      print(' ', end= '')
  print()


