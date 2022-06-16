
#내 답
def solution(id_list, report, k):
    import numpy as np

    mtx = np.zeros((len(id_list),len(id_list)))

    for rep_nm  in report:
        reporter = rep_nm.split(" ")[0]
        reported = rep_nm.split(" ")[1]
        mtx[id_list.index(reporter),id_list.index(reported)] = 1

    reported_num= np.sum(mtx, axis=0)
    paused_idx = np.where(reported_num>= k)


    answer = list(np.sum(mtx[:, paused_idx[0]],axis=1))


    return answer

#추천 답안
def solution2(id_list, report, k):
  answer= [0] * len(id_list)
  reports = {x: 0  for x in id_list}

  for r in set(report):
    reports[r.split()[1]] += 1

  for r in set(report):
    if reports[r.split()] >= k:
      answer[id_list.index(r.split()[0])] += 1

  return answer