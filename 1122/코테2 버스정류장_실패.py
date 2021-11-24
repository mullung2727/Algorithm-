
id = 0
id_ls = [0 for _ in range(101)]
finished = [False for _ in range(101)]
stack = []
SCC = []

def dfs(x, dic):
    global id
    id += 1
    id_ls[x] = id
    stack.append(x)
    parent = id
    nodes = dic[x]
    for node in nodes:
        if id_ls[node] == 0:
            parent = min(parent, dfs(node, dic))
        elif not finished[node]:
            parent = min(parent, id_ls[node])

    if parent == id_ls[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)
    return parent

def bfs(dic, idx, n):
    result = [0 for _ in range(n)]
    q = dic[idx].copy()
    start = idx
    while q:
        end = q.pop(0)
        if result[end-1] == 0:
            # print(start, end)
            result[end-1] = 1
            q.extend(dic[end])

    return result


def solution(n,signs):

    dic = {i:[] for i in range(1, n+1)}
    for i in range(1,n+1):
        for j in range(1,n+1):
            if signs[i-1][j-1] == 1:
                dic[i].append(j)
    for i in range(1, n+1):
        if id_ls[i] == 0:
            dfs(i, dic)
    circle = set()
    for scc in SCC:
        if len(scc) > 1:
            for start in scc:
                circle.add(start)
                for end in scc:
                    signs[start-1][end-1] = 1

    for i in range(1, n + 1):
        if i not in circle:

            result = bfs(dic, i, n)
            for end in range(n):
                if result[end] == 1:
                    signs[i-1][end] = 1
    return signs


n=3
signs= [[0,0,1],[0,0,1],[0,1,0]]
print(solution(n, signs))