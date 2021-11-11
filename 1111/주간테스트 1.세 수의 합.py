prime_ls = [None for _ in range(100000001)]
for i in range(2,100000001):
    if prime_ls[i] == None:
        prime_ls[i] = True
        for j in range(i*i, 100000001, i):
            prime_ls[j] = False

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i):
            for k in range(j):
                if prime_ls[nums[i]+nums[j]+nums[k]] == True:
                    answer+= 1
    return answer
for i in range(2, 100000001):
    if prime_ls[i] == True:
        print(i, end = ' ')