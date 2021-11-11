def solution(arr):
    if len(set(arr)) == 1:
        return list(set(arr))
    answer = [arr[i] for i in range(len(arr)-1) if arr[i+1] != arr[i]]
    if arr[-1] != answer[-1]:
        answer.append(arr[-1])
    return answer
a = [1,1]
print(solution(a))