
def solution(board, moves):
    answer = 0
    basket = []
    
    #바구니에 담기는 인형순서를 basket리스트에 저장한다
    for i in moves:
        for j in range(0,len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                #바구니에 넣은 인형의 자리는 0으로 바꿔준다.
                board[j][i-1] =0
                break
    
    #basket에 담긴 인형 중에 같은 인형이 연속해서 쌓인 횟수를 도출한다.    
    
    i =1
    while i <len(basket):
        if basket[i] == basket[i-1]:
            #중복된 인형을 바구니에서 제거한다
            basket.pop(i-1) 
            basket.pop(i-1) 
            answer += 2
            i = 1
            
            
        else:
            i += 1            
    
    return answer

