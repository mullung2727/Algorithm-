def change(n):
    v = '124'
    result = ''
    while n > 0:
        n, mod = divmod(n,3)
        result += v[mod]
    return result[::-1]

def solution(n):
    power = 0
    while n >= 0:
        n -= 3**power
        power += 1
    n += 3**(power-1)
    answer = change(n)
    answer = '1'*(power-1-len(answer)) + answer#.replace('2','4').replace('1','2').replace('0','1')

    return answer