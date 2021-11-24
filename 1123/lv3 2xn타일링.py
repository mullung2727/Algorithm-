import sys
sys.setrecursionlimit(100000)
result = [ 0 for _ in range(60001)]
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if result[n] != 0:
        return result[n]
    answer = solution(n-1) + solution(n-2)
    result[n] = answer % 1000000007
    return answer

print(solution(1000))