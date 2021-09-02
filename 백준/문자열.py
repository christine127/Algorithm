#아스키코드
print(ord(input()))

#숫자의 합
input()
print(sum(map(int,input())))

#알파벳 찾기
from string import ascii_lowercase
S = list(input())
alpha = list(ascii_lowercase)
alpha_loc = ['-1'] * 26

for i in range(26):
  if alpha[i] in S:
    alpha_loc[i] = str(S.index(alpha[i]))

print(" ".join(alpha_loc))