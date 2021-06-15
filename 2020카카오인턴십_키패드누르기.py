def solution(numbers, hand):
    answer = ''
    
    # 2,5,8,0 키패드를 눌러야 할 때 이전 키패드와의 거리 구하기 
    def distance(n,d): #n:start, d:destination 
        if n == d :
            distance =0
        
        elif (n==0)|(d == 0) :
            if abs(n-d) ==8 :
                distance =1
            elif (abs(n-d)>= 7) | (abs(n-d)==5):
                distance =2
            elif (abs(n-d) >3) | (abs(n-d)==2):
                distance = 3
            else:
                distance =4
        
        else:
            if (abs(n-d) == 1) |(abs(n-d)==3):
                distance =1
            elif (abs(n-d) <5) | (abs(n-d) ==6):
                distance = 2
            else: 
                distance = 3
                
        return distance
    
        
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer = answer+"L"
        elif numbers[i] in [3,6,9]:
            answer=  answer+"R"
        else:
            if i ==0 :
                answer = hand[0].upper()
            elif len(set(answer)) ==1:
                st_1 = distance(numbers[i-1], numbers[i]) 
                st_0 = distance(numbers[i],0)+1
                
                if st_1 == st_0:
                    answer = answer+hand[0].upper()
                elif st_1 < st_0:
                    answer = answer+ answer[i-1]
                else:
                    next = {"L","R"}- set(answer)
                    answer = answer+ list(next)[0]
            else:
                st_1 = distance(numbers[i-1], numbers[i]) 
                the_other_hand = {"L","R"}- set(answer[i-1])
                                              
                the_loc = answer.rfind(list(the_other_hand)[0])
                st_2 = distance(numbers[the_loc], numbers[i])
                print(i, numbers[i],"--------------------")
                print(numbers[i-1], answer[i-1],st_1)
                print(numbers[the_loc],the_other_hand,st_2)


                if st_1 == st_2:
                    answer = answer+hand[0].upper()
                elif st_1 < st_2:
                    answer = answer+ answer[i-1]
                else:
                    answer = answer+ list(the_other_hand)[0]
                print(answer)
          
    return answer