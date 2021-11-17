from itertools import permutations


def solution(numbers):
    s_numbers = [str(i) for i in numbers]
    s_numbers.sort(key= lambda x: x*4, reverse=True)
    return str(int(''.join(s_numbers)))

nums = [3, 30, 34, 5, 9]
print(solution(nums))
