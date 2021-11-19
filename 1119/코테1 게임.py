def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(a)):
        if B[i] > A[i]:
            answer += 1


    return answer


a, b = [5,1,3,7],	[2,2,6,8]
print(solution(a,b))
