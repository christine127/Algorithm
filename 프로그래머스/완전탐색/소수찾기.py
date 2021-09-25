#내 답
def prime_number(n):
    a = [False,False]+[True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if a[i] == True:
            primes.append(i)
            for j in range(2*i,n+1,i):
                a[j] = False
    return primes

from itertools import permutations

def solution(numbers):
    answer = 0
    arr = []
    for i in range(1,len(numbers)+1):
        arr.extend(list(permutations(numbers,i)))

    new = set()
    for i in arr:
        a = ''.join(list(i))
        new.add(int(a))

    primes = prime_number(max(new))

    for i in new:
      if i in primes:
        answer += 1
        
    return answer

  
#다른 사람 답
from itertools import permutations

def solution(n):
  a = set()
  for i in range(len(n)):
    a |= set(map(int,map("".join, permutations(list(n), i+1))))
  a -= set(range(0,2))
  for i in range(2, int(max(a)**0.5)+1):
    a -= set(range(i*2, max(a)+1, i))

  return len(a)


