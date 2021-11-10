def check_correct(p):
    while p.replace("()",'',1) != p:
        p = p.replace("()",'',1)
    return True if p == '' else False

def split_uv(p):
    cnt_l = 0
    cnt_r = 0
    idx = 0
    while cnt_l == 0 or cnt_l != cnt_r:
        if p[idx] == '(':
            cnt_l +=1
        else:
            cnt_r +=1
        idx += 1
    u = p[:idx]
    v = p[idx:]
    return u, v
def revers_paren(u):
    result = ''
    for i in u[1:-1]:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    if check_correct(p):
        return p
    u, v = split_uv(p)
    if check_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + revers_paren(u)

a=")("
print(solution(a))