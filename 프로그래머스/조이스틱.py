from string import ascii_uppercase
import numpy as np

## 0
def solution(name):
    answer = 0
    alpha_list = list(ascii_uppercase)
    number_list =  [abs(i-26) if i> 13 else i for i in range(26)]
    alpha_dict = dict(zip(alpha_list, number_list))

    name_list = list(name)
    alpha_to_num = list(np.vectorize(alpha_dict.get)(name_list))
    alpha_to_num = [int(i) for i in alpha_to_num]
    answer = sum(alpha_to_num) + len(alpha_to_num) -1

    if 0 in alpha_to_num: 
        index_queue = alpha_to_num.copy()
        packet = []
        tmp = []
        i = 0 
        idx = [0]
        v = index_queue.pop(0)
        tmp.append(v)

        while index_queue:
          vv = index_queue.pop(0)
          if v == vv:
            tmp.append(vv)
            i += 1
          else:
            i += 1
            packet.append(tmp)
            idx.append(i)
            tmp = []
            tmp.append(vv)
            v = vv
        packet.append(tmp)
        packet_len = [len(i) for i in packet]

        if idx[packet_len.index(max(packet_len))] < max(packet_len):
          answer = answer + idx[packet_len.index(max(packet_len))] - max(packet_len)

    return answer



## 1

def solution_1(name):
    answer = 0
    alpha_list = list(ascii_uppercase)
    number_list =  [abs(i-26) if i> 13 else i for i in range(26)]
    alpha_dict = dict(zip(alpha_list, number_list))

    name_list = list(name)
    name_to_num = list(np.vectorize(alpha_dict.get)(name_list))
    name_to_num = [int(i) for i in name_to_num]
    answer = sum(name_to_num) + len(name_to_num) -1

    if 0 in name_to_num: 
        index_list = list(filter(lambda x: name_to_num[x] == 0, range(len(name_to_num))))
        index_shift = index_list.copy()
        index_shift.pop(0)
        index_shift.append(0)
        index_list = np.array(index_list) - np.array(index_shift)
        

        minus1 = list(filter(lambda x: x ==-1 , index_list))
        answer -= len(minus1) +1
    


    return answer