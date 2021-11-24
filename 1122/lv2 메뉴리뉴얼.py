from itertools import combinations

def solution(orders, course):
    dic = {}
    for order in orders:
        for n_menu in course:
            combi = list(combinations(order, n_menu))
            for candi in combi:
                candi = ''.join(sorted(candi))
                if dic.get(candi) != None:
                    dic[candi] += 1
                else:
                    dic[candi] = 1
    sol = {c:([''], 0) for c in course}
    for key, val in dic.items():
        if val > 1:
            len_key = len(key)
            # print(sol[len_key], key)
            if val > sol[len_key][1]:
                sol[len_key] = ([key], val)
            elif val == sol[len_key][1]:
                sol[len_key][0].append(key)
    answer = []
    for i in sol.values():
        if i[0] != [""]:
            answer.extend(i[0])
    answer.sort()
    return answer


o = ["XYZ", "XWY", "WXA"]
c = [2,3,4]

answer = solution(o,c)
print(solution(o,c))