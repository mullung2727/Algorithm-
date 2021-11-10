def solution(record):
    nick_dic = {}
    actions = []
    for i in record:
        s_record = i.split()

        if s_record[0] == "Leave":
            actions.append((0, s_record[1]))

        elif s_record[0] == "Enter":
            nick_dic[s_record[1]] = s_record[2]
            actions.append((1, s_record[1]))
        else:
            nick_dic[s_record[1]] = s_record[2]
    answer = []
    for i in actions:
        if i[0] == 0:
            answer.append(f"{nick_dic[i[1]]}님이 나갔습니다.")
        else:
            answer.append(f"{nick_dic[i[1]]}님이 들어왔습니다.")



    return answer


answer = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
for i in answer:
    print(i)