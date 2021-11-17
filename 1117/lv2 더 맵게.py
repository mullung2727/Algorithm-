import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >=2 and scoville[0] < K:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + (food2*2))
        answer += 1
    if scoville[0] < K:
        return -1
    return answer