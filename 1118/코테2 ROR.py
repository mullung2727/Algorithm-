def bfs(visited, maps, steps):
    len_x = len(visited)
    len_y = len(visited[0])
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    start = [0, 0]
    q = [start]
    while q:
        x, y = q.pop(0)
        visited[x][y] = True
        for dx, dy in move:
            if 0 <= x + dx < len_x and 0 <= y + dy < len_y and maps[x + dx][y + dy] == 1 and visited[x + dx][y + dy] == False:
                q.append([x + dx, y + dy])
                steps[x + dx][y + dy] = steps[x][y] + 1
    return steps[len_x-1][len_y-1]


def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    steps = [[1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    answer = bfs(visited, maps, steps)
    if answer == 1:
        return -1
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))