def time_to_seconds(time):
    mm,nn = time.split(":")
    mm = int(mm)
    nn = int(nn)
    seconds = mm*60 + nn
    
    return seconds


def solution(video_len, pos, op_start, op_end, commands):
    #-- pos, op_start, op_end를 초로 변환하기
    pos_s = time_to_seconds(pos) 
    op_start_s = time_to_seconds(op_start)
    op_end_s = time_to_seconds(op_end)
    video_len_s = time_to_seconds(video_len)
        
    answer_s = pos_s

    
    for command in commands:
        if answer_s >= op_start_s and answer_s <= op_end_s :
            answer_s = op_end_s
        else: 
            pass

        if command == "prev":
            ## max 로 대체 가능 
            if answer_s < 10:
                answer_s = 0
            else:
                answer_s -= 10
        else:
            ## min으로 대체 가능
            if (video_len_s - answer_s) <10:
                answer_s = video_len_s
            else :
                answer_s += 10
            
    if answer_s >= op_start_s and answer_s <= op_end_s :
        answer_s = op_end_s
    else: 
        pass
    

    mm = f"{answer_s// 60:02d}"
    nn = f"{answer_s % 60:02d}"
    
    answer = mm+":"+nn


    return answer
