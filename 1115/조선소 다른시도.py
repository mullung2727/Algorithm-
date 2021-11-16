# 가장 큰 수 찾는다
# 그다음 큰 수 찾는다
# 두 수의 차이만큼 빼고 no도 감소
# 이제 가장 큰 수는 2개
# 그 다음 큰 수를 찾는다
# 두 수의 차이만큼 빼고 no*2 감소
# 이제 가장 큰 수는 3개 -- 반복, no가 0보다 클때까지

import heapq

def solution(no, works):
    hq = [-work for work in works]
    heapq.heapify(hq)
    max_num = heapq.heappop(hq) * -1
    cnt = 1
    while hq:
        print(hq, cnt)
        next_num = heapq.heappop(hq) * -1
        if no <= (max_num - next_num) * cnt:
            heapq.heappush(hq, next_num*-1)
            break
        no -= (max_num - next_num) * cnt
        cnt += 1
        max_num = next_num
    print(1111, max_num, cnt, no)

    div, mod = divmod(no, cnt)
    max_num -= div
    if not hq:
        if max_num <= 0:
            return 0
        else:
            result = max_num ** 2 * (cnt-mod) + (max_num-1) ** 2 * mod
            return result
    else:
        result = max_num ** 2 * (cnt - mod) + (max_num - 1) ** 2 * mod
        for i in hq:
            result += i ** 2
        return result


no = 4
works = [4,3,3]

print(solution(no, works))

