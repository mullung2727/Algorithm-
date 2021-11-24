def check(idx, s):
    # 홀수 확인
    odd_cnt = -1
    right_idx = idx
    left_idx = idx
    while left_idx >=0 and right_idx < len(s) and s[left_idx] == s[right_idx] :
        odd_cnt += 2
        left_idx -= 1
        right_idx += 1

    even_cnt = 0
    right_idx = idx+1
    left_idx = idx
    while left_idx >=0 and right_idx < len(s) and s[left_idx] == s[right_idx] :
        even_cnt += 2
        left_idx -= 1
        right_idx += 1
    return max(odd_cnt, even_cnt)

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer = max(answer, check(i, s))

    return answer