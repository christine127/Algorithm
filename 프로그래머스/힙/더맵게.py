import heapq
def solution(scoville, K):
    answer = 0
    scoville_idx = 0
    heapq.heapify(scoville)
    
    while (len(scoville) > 1):
        min1= heapq.heappop(scoville)
        if min1 >= K:
            return answer
        min2= heapq.heappop(scoville)
        scoville_idx = min1 + (2*min2)
        answer += 1
        heapq.heappush(scoville,scoville_idx)
        
    if len(scoville) == 1 and scoville[0] >= K:
        return answer
        
    return -1