import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    first = heapq.heappop(scoville)
    while first < K:
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2 * second)
        answer += 1
        if len(scoville) == 1:
            break
        first = heapq.heappop(scoville)
    if len(scoville) == 1 and heapq.heappop(scoville) < K:
        return -1
    return answer
