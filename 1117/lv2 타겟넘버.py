answer = 0
def dfs(numbers, target):
    global answer
    numbers_copy = numbers[:]

    num = numbers_copy.pop()
    if not numbers_copy:
        print(target, num)
        if target == num:
            answer += 1
        elif target == -num:
            answer += 1
    else:
        dfs(numbers_copy, target + num)
        dfs(numbers_copy, target - num)
def solution(numbers, target):
    dfs(numbers, target)
    return answer
