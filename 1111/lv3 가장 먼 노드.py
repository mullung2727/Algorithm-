def bfs(start):
    visited[start] = True
    q = [(start, 0)]
    visit_cnt[start] = 0
    while q:
        node, cnt = q.pop(0)
        print(node, cnt)
        for i in lines[node]:
            if visited[i] == False:
                q.append((i, cnt + 1))
            else:
                if not visit_cnt.get(i):
                    visit_cnt[i] = cnt


def solution(n, edge):
    global visited, lines, visit_cnt
    visited = [None] + [False for _ in range(n)]
    lines = [[] for _ in range(n + 1)]
    visit_cnt = {}
    for s, e in edge:
        lines[s].append(e)
        lines[e].append(s)

    bfs(1)
    max_val = 0
    max_cnt = 0
    for key, value in visit_cnt.items():
        if value > max_val:
            max_val = value
            max_cnt = 1
        elif value == max_val:
            max_cnt += 1
    return max_cnt

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))