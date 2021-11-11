def check(skill, skill_tree):
    idx_ls = []
    for i in skill:
        idx = skill_tree.find(i)
        if idx == -1:
            idx_ls.append(100)
        else:
            idx_ls.append(idx)
    return idx_ls == sorted(idx_ls)

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        answer += check(skill, i)
    return answer

skill = "CBD"
skill_trees = 	["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))