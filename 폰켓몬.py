def solution(nums):
    #가장 종류가 많은 조합 수 구하기
    answer = 0
    s = set(nums)
    
    if len(s) >len(nums) /2:
        answer = len(nums)/2
    else:
        answer = len(s)
    
    return answer