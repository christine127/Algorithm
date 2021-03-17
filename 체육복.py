def solution(n, lost, reserve):
    #전체 인원수-  체육복 두고 온 사람
    answer= n-len(lost)
    # print("처음" , answer)
    
    #여벌이 있는 학생이 도난당했을 경우, 남은 체육복이 하나이므로 빌려줄 수 없다
    #교집합을 통해 해당하는 학생 수를 구하고 각 리스트에서 제외시킨다
    inter = list(set(lost).intersection(set(reserve)))
    lost1 = list(set(lost).difference(set(reserve)))
    reserve1 = list(set(reserve).difference(set(lost)))
    #교집합에 있는 인원수만큼 answer에 더해줌.
    if len(inter) >0:
        answer += len(inter)
        
    # print(lost1,reserve1)
    
    #reserve에 해당되는 학생과 lost에 해당하는 학생의 자리 간격이 1일 때, answer에 더해준다.
    for j in range(0,len(reserve1)):
        for i in range(0,len(lost1)):
            if abs(lost1[i]-reserve1[j]) == 1:
                answer += 1
                # print(reserve1[j],lost1[i],answer)
                lost1.pop(i) #빌린 학생의 경우 리스트에서 제외시킨다.
                break #빌려준 학생에서 다음학생으로 넘어감.
             
        

    return answer