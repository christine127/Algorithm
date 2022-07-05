#나의 답안

def getMyDivisor(n):
    divisorList = []
    for i in range(1, int(n**(1/2))+1):
        if (n % i == 0):
            divisorList.append([n//i,i])
    return divisorList

def solution(brown,yellow):
    y_lst = getMyDivisor(yellow)
    t_lst = getMyDivisor(brown+yellow)
    for i in t_lst:
        for j in y_lst:
            if (j[0]+2 == i[0]) and (j[1]+2 == i[1]):
                return i

#다른 사람 풀이
def solution(brown,yellow):
  for i in range(1, int(yellow)**(1/2)+1):
    if yellow % i == 0 :
      if 2*(i+ yellow//i) == brown - 4:
        return [yellow//i+2, i+2]
              