from string import ascii_uppercase
import numpy as np

## 0
def solution_FAILED(name):
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
        print(packet)
        packet_len = [len(i) for i in packet]
        print(packet_len)
        
        list_A = list(filter(lambda x: 0 in x, packet))
        A_len = [len(i) for i in list_A]
        print(list_A)

        
        # if idx[packet_len.index(max(list_A))] < max(list_A):
          # answer = answer + idx[packet_len.index(max(packet_len))] - max(packet_len)

    return answer


## 1

def solution_1(name):
  change = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
  idx = 0
  answer = 0
  while True:
    answer += change[idx]
    change[idx] = 0
    if sum(change) == 0:
      return answer
    
    left, right = 1, 1
    while change[idx - left] == 0:
      left += 1
    while change[idx + right] == 0:
      right += 1
    answer += left if left < right else right
    idx += -left if left < right else right

def solution_ANSWER(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer
