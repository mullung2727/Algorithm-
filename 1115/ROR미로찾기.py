def bfs(n, m, maps):
    visited = [[False for _ in range(m)] for __ in range(n)]
    cnt_ls = []
    check = [[1 for _ in range(m)] for __ in range(n)]
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    visited[0][0] = True
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                if maps[next_x][next_y] == 1 and visited[next_x][next_y] == False:
                    check[next_x][next_y] = check[x][y] + 1
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y))
    return check[n - 1][m - 1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(n, m, maps)
    return answer if answer != 1 else -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))