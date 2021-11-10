def change(s):
    s = s.split()
    h, m, ss = map(float, s[1].split(':'))
    print(h,m,ss, float(s[2][:-1]))
    t = h * 3600 + m * 60 + ss
    return ([t - float(s[2][:-1]) + 0.001, t + 1])

def solution(lines):
    ls = []
    for i in lines:
        s_i = i.split()
        h, m, s = map(float, s_i[1].split(':'))
        t = h*3600+m*60+s
        ls.append([t-float(s_i[2][:-1])+0.001,t+1])
    ls.sort()
    max_cnt = 0
    for start, end in ls:
        cnt = 0
        for start2, end2 in ls:
            if start2 <= end <= end2:
                cnt += 1
        max_cnt = cnt if cnt > max_cnt else max_cnt

    return max_cnt, ls

q = ["2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"]
s, ls = solution(q)
print(s, ls)
print(change(q[0]))