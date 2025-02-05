def solution(diffs, times, limit):
    total_time = limit+1
    answer = 1
    
    while limit < total_time :
        total_time = times[0]
        
        for i in range(1,len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1]

            if diff > answer :
                n = diff - answer
                t = time_cur + time_prev
                total_time += n*t  
            total_time += time_cur
        answer += 1
    answer -= 1    
    return answer
