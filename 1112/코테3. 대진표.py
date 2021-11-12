#대진표에서 a, b가 계속 승리했을 때 몇번째에 만나는가?
# 1
# 1 2
# 1 2 3 4 ex)3,4번 대결-> 승자가 결승전에서 2번이 된다.
def next_n(n):
    if n%2:
        n +=1
    return n // 2

def solution(n,a,b):
    answer = 0
    while a != b:
        a = next_n(a)
        b = next_n(b)
        answer+=1

    return answer