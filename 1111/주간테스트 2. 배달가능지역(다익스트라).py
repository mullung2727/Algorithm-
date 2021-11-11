from queue import PriorityQueue

def bfs(start):

    pq = PriorityQueue()
    pq.put((0,start))
    while not pq.empty():
        dist, node = pq.get()
        dist *= -1

        if cost[node] < dist:
            continue

        for i in road_info[node]:
            next_node = i[1]
            next_dist = i[0] + dist
            if cost[next_node] > next_dist:
                cost[next_node] = next_dist
                pq.put((-next_dist, next_node))


def solution(N, road, K):
    global road_info, cost

    INF = 10000000

    road_info = [[] for _ in range(N+1)]
    cost = [None] +[INF for i in range(N)]
    cost[1] = 0
    for a, b, c in road:
        for cc, bb in road_info[a]:
            if b == bb and c < cc:
                road_info[a].remove((cc,b))
                road_info[b].remove((cc,a))
        road_info[a].append((c,b))
        road_info[b].append((c,a))
    print(road_info)
    bfs(1)
    cnt = 0
    for i in cost[1:]:
        if i <= K:
            cnt+=1

    return cnt