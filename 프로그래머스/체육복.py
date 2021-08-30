def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    new_lost.sort()
    new_reserve.sort()
    
    for l in new_lost:
        compare= list(map(lambda x:abs(x-l) , new_reserve))
        if 1 in compare:
            idx = compare.index(1)
            new_reserve.remove(new_reserve[idx])            
        else: 
            n -= 1
         
    return n