##문자열다루기 기본 CODING TEST
##문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
##예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
def solution(s):
    ##answer 초기값 설정
    answer = True
    ##문자열 s 길이가 4혹은 6인지 확인
    if len(s) != 4 and len(s) != 6:
        answer = False
    else:
        ##숫자로만 구성되어있는지 확인
        if s.numeric() != True:
            answer = False
    
    return answer