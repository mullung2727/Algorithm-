def solution(arr):
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])
    answer = 1
    start, end = arr[0]
    for i in range(1, len(arr)):
        s_i, e_i = arr[i]
        if end <= s_i:
            answer += 1
            end = e_i

    return answer