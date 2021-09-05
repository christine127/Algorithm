#아스키코드
print(ord(input()))

#숫자의 합
input()
print(sum(map(int,input())))

#알파벳 찾기
from string import ascii_lowercase
alpha = list(ascii_lowercase)
S = list(input())

for a in alpha:
  if a in S:
    print(S.index(a), end = ' ')
  else:
    print('-1', end = " ")

#문자열 반복
N = int(input())
matrix = [[0]* 2 for _ in range(N)]
for i in range(N):
  matrix[i] = list(input().split(' '))

for i in range(N):
  for j in range(len(matrix[i][1])):
    print(matrix[i][1][j] * int(matrix[i][0]),end ="")
  print('')

#단어 공부
#내 답안
vocab = input().upper()
letter =set(vocab)
idx = dict((i,vocab.count(i)) for i in letter)
max_key = [k for k,v in idx.items() if max(idx.values())== v]
if len(max_key)>1:
  print("?")
else:
  print(max_key[0])

#다른 답안
s,a = input().lower(),[]
for i in range(97,123):
  a.append(s.count(chr(i)))
print('?' if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())