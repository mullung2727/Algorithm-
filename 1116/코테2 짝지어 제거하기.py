def solution(s):
    if len(s) % 2 == 1:
        return 0
    ls = [s[0]]
    for i in s[1:]:
        if len(ls) > 0 and ls[-1] == i:
            ls.pop()
        else:
            ls.append(i)
    if ls:
        return 0
    return 1