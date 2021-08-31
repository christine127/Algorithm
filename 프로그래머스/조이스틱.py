from string import ascii_uppercase
import numpy as np
alpha_list = list(ascii_uppercase)
number_list =  [abs(i-26) if i> 13 else i for i in range(26)]

alpha_dict = dict(zip(alpha_list, number_list))

name = "KANNEKANANNAAAKKK"
name_list = list(name)
name_to_num = list(np.vectorize(alpha_dict.get)(name_list))
index_list = list(filter(lambda x: name_to_num[x] == 0, range(len(name_to_num))))
