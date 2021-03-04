def solution(n):    
    sieve = [True] * (n+1)
    #n의 최대 약수가 sqrt(n)이하이므로 m=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range (2, m + 1):
        if sieve[i] == True: 
            for j in range(2*i,n+1, i): 
                sieve[j] = False
                
    answer= len([i for i in range(2,n+1) if sieve[i] == True])

    return answer

