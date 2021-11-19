def bfs(s_x, s_y, place):
    print(s_x, s_y, "check start!!!")
    visited = [[False for _ in range(5)] for _ in range(5)]
    step = [[0 for _ in range(5)] for _ in range(5)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [(s_x, s_y)]
    visited[s_x][s_y] = True
    while q:
        x, y = q.pop(0)
        if step[x][y] >= 2: continue
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x <= 4 and 0 <= next_y <= 4:
                if place[next_x][next_y] == "P" and visited[next_x][next_y] == False:
                    print(next_x, next_y, visited[next_x][next_y])
                    return False
                if not visited[next_x][next_y] and place[next_x][next_y] == "O":
                    visited[next_x][next_y] = True
                    step[next_x][next_y] = step[x][y] + 1
                    q.append((next_x, next_y))
    return True


def check(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                if not bfs(x, y, place):
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))

    return answer
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]
print(solution(places))