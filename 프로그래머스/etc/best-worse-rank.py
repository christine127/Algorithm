def solution(lottos, win_nums):

    zero_cnt = 0
    correct_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        elif i in win_nums:
            win_nums.remove(i)
            correct_cnt += 1

    answer = [min(7 -(correct_cnt + zero_cnt),6),min(7 - correct_cnt,6)]

    return answer
