
def solution(n, times):
    waiting = times.copy()
    using = [False for _ in range(len(times))]
    time = 0
    while n > 0:
        for i in range(len(waiting)):
            if waiting[i] <= 0:
                waiting[i] = 0
                using[i] = False
        min_num = min(waiting)
        min_idx = waiting.find(min_num)
        if using[min_idx]:
            time += min_num
            waiting = [ i-min_num for i in waiting]


    answer = 0
    return answer