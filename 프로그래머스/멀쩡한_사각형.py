def solution(w,h):
    #최대공약수 구하기
    number = max(w,h)
    divisor = min(w,h)
    while (number % divisor) !=0:
        remainder =number % divisor
        number =divisor
        divisor = remainder
    
    #가로*세로 - (가로+세로-최대공약수)
    answer = w*h -(w+h-divisor)
    
    return answer
    