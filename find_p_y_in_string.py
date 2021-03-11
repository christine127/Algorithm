def solution(s):
    answer = True
    s = s.lower()
    p = s.count("p")
    y = s.count("y")
    
    if p != y:
        answer= False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer