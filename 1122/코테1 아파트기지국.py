def split(n, stations, w):
    result = []
    if stations[0]-w <= 1:
        s = stations.pop(0)
        start = s+w+1
    else:
        start = 1

    for s in stations:
        length = (s-w) - start
        if length > 0:
            result.append(length)
        start = s+w+1
    if n > start:
        result.append(n+1-start)
    return result

def solution(n, stations, w):
    need = split(n, stations, w)
    answer = 0
    interval = w*2+1
    for i in need:
        div, mod = divmod(i, interval)
        answer += div
        if mod > 0:
            answer += 1


    return answer, need

n = 16
stations = [3]
W = 2
print(solution(n, stations, W))