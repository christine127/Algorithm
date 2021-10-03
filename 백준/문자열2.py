#단어의 개수
word = input().split()
print(len(word))

#상수
a,b = input().split()
A = a[::-1]
B = b[::-1]
print(max(A,B))

#다이얼
def func(x):
  if x =='S':
    return 7
  elif x =='V': 
    return 8
  elif x =='Y' or x == 'Z': 
    return 9
  return (ord(x)-59)//3


lst = list(map(func,input()))

print(sum(lst)+len(lst))

# print(sum((ord(i)-62-(i in 'SVYZ')-(i=='Z'))//3+2 for i in input()))