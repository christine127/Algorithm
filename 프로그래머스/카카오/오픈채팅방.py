def solution(record):
    a = list(filter(lambda x: x.startswith("Enter")|x.startswith("Change"), record))
    answer = []
    id_dict = {}

    i = 0
    for line in a:
        id = line.split(" ")[1]
        id_dict[id] = i
        i += 1

    j = 0
    for id in id_dict:
        name = a[id_dict[id]].split(" ")[-1]
        id_dict[id] =  name


    for r in record:
        if r.startswith("Change"):
            continue
        elif r.startswith("Enter"):
            answer.append(id_dict[r.split()[1]]+"님이 들어왔습니다.")
        else:
            answer.append(id_dict[r.split()[1]]+"님이 나갔습니다.")


    
    return answer