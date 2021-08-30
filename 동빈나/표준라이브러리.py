#Itertools
#순열과 조합
#순열 : 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열하는 것
#조합 : 서로다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것

#순열
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))
# print(result)

#조합
from itertools import combinations
result = list(combinations(data,2))
# print(result)

#중복순열: 중복허용을 의미
from itertools import product
result = list(product(data, repeat=2))
print(result)

#중복조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2))
print(result)


#Counter - 등장 횟수를 세는 기능
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

#math
#최대공약수(GCD), 최소공배수
import math
def lcm(a,b):
  return a*b//math.gcd(a,b)

a=21
b=14
print(math.gcd(a,b))
print(lcm(a,b))