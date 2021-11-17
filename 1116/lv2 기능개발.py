def solution(progresses, speeds):
    cnt_ls = []
    for progress, speed in zip(progresses, speeds):
        cnt = 0
        while progress < 100:
            progress += speed
            cnt += 1
        cnt_ls.append(cnt)

    answer = []
    realese_num = 1
    a = cnt_ls[0]
    for job in cnt_ls[1:]:
        if job <= a:
            realese_num += 1
        else:
            answer.append(realese_num)
            a = job
            realese_num = 1
    answer.append(realese_num)
    return answer