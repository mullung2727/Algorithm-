def check(s):
    len_s = len(s)
    # if len_s == 1:
    #     return True
    if len_s % 2: # 홀수
        if s[:len_s//2] == s[len_s//2+1:][::-1]:
            return True
        else:
            return False
    else: # 짝수
        if s[:len_s//2] == s[len_s//2:][::-1]:
            return True
        else:
            return False
def solution(n,m):
    answer = 0
    for i in range(n,m+1):
        answer += check(str(i))

    return answer

print(solution(10201,10201))
print(check('1'))