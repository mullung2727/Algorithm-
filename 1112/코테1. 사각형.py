# 세 점이 주어졌을 때 직사각형이 되도록 나머지 점을 찾아라

def solution(v):
    answer = []
    x_ls = []
    y_ls = []
    for x, y in v:
        x_ls.append(x)
        y_ls.append(y)
    x = x_ls.pop()
    if x in x_ls:
        x_ls.remove(x)
        x = x_ls[0]

    y = y_ls.pop()
    if y in y_ls:
        y_ls.remove(y)
        y = y_ls[0]

    return [x,y]