import copy


def solution(board):
    x_len = len(board)
    y_len = len(board[0])
    if x_len <= 1:
        return max(board[0])
    if y_len <= 1:
        return max([v for v in board[i][0]])
    check_board = copy.deepcopy(board)
    max_v = 0
    for x in range(1, x_len):
        for y in range(1, y_len):
            if board[x][y] == 1:
                v = min(check_board[x - 1][y], check_board[x][y - 1], check_board[x - 1][y - 1]) + 1
                check_board[x][y] = v
                max_v = max(v, max_v)
            else:
                check_board[x][y] == 0

    return max_v ** 2

board = [[0,0,1,1],[1,1,1,1]]
print(solution((board)))