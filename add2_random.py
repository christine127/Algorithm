def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):        
        for j in range(i+1, len(numbers)):
            a =numbers[i] + numbers[j]
            if not a in answer:
                answer.append(a)        
    answer.sort()
    return answer