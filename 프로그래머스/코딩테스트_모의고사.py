

def solution(answers):
    answer = []
    ## 먼저 학생 1,2,3의 답안이 있는 리스트를 준비한다.
    std1=[]
    std2=[]
    std3=[]
    
    #학생 1 답안의 패턴: (1,2,3,4,5) 반복
    for i in range(len(answers)):
        if (i % 5) ==0:
            std1.append(1)
        elif (i % 5) ==1:
            std1.append(2)
        elif (i % 5) ==2:
            std1.append(3)
        elif (i % 5) ==3:
            std1.append(4)
        else:
            std1.append(5)
            
    #학생2 답안의 패턴 :(2,1,2,3,2,4,2,5) 반복
    for i in range(len(answers)):
        if (i % 2) == 0:
            std2.append(2)
        elif (i % 8) == 1:
            std2.append(1)
        elif (i % 8) == 3:
            std2.append(3)
        elif (i % 8) == 5:
            std2.append(4)
        elif (i % 8) == 7:
            std2.append(5)
            
    #학생 3 답안의 패턴 :(3,3,1,1,2,2,4,4,5,5) 반복
    for i in range(len(answers)):
        if (i % 10) == 0 or (i % 10) ==  1:
            std3.append(3)
        if (i % 10) == 2 or (i % 10) == 3:
            std3.append(1)
        if (i % 10) == 4 or (i % 10) == 5:
            std3.append(2)
        if (i % 10) == 6 or (i % 10) == 7:
            std3.append(4)
        if (i % 10) == 8 or (i % 10) == 9:
            std3.append(5)
    
    #각 학생의 정답 개수를 표현하는 변수를 만든다.(cr* =학생*이 맞은 개수)
    cr1=0
    cr2=0
    cr3=0 
    
    #각 학생의 답안과 정답을 비교하여 맞은 개수를 추출한다.
    
    for i in range(len(answers)):
        if answers[i] == std1[i]:
            cr1 += 1
    for i in range(len(answers)):
        if answers[i] == std2[i]:
            cr2 += 1
    for i in range(len(answers)):
        if answers[i] == std3[i]:
            cr3 += 1
    
    a= [cr1,cr2,cr3]
    b= list(enumerate(a))

    #가장 많이 맞은 학생 수 리스트 출력
    for i in b:
        if i[1] == max(a):
            answer.append(i[0]+1)
    
    return answer


# In[ ]:




