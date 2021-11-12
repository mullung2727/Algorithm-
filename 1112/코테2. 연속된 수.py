# 제시된 arr이 1~N까지 중복없이, 빠짐없이 있는가?
def solution(arr):

    return sorted(arr) == list(range(1,len(arr)+1))