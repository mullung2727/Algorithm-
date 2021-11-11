# x번째 행에 놓은 퀸에 대해 검증
def check(x):
    # 이전 행에서 놓았던 모든 퀸들을 확인
    for i in range(x):
        # 위쪽 혹은 대각선 확인
        if row[x] == row[i]:
            return False
        if abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x, n):
    global result
    # 체스판의 마지막 행에 도착한 경우
    if x == n:
        result += 1
    else:
        # x번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            # 해당 위치에 Queen을 두어도 괜찮은 경우
            if check(x):
                # 다음 행으로 넘어가기
                dfs(x+1, n)


def solution(n):
    global row, result
    result = 0
    row = [0] * n
    dfs(0, n)
    return result
print(solution(3))
# 알고리즘 너무 복잡.. https://pythontutor.com/visualize.html#mode=display 에서 확인하자
# row의 의미: 각 열의 숫자는 행의 위치를 말함
# ex) n=3 일때 [1, 2, 2] ->