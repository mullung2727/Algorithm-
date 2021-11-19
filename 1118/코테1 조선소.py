def solution(no, works):
    if no >= sum(works): return 0
    for i in range(no):
        works.sort()
        works[-1] -= 1

    result = 0
    for work in works:
        result += work ** 2
    return result