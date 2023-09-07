def solution(citations):
    answer = 0
    citations = list(reversed(sorted(citations)))
    for i in range(len(citations)):
        gap = len(citations) - i
        if gap <= (i+1) and citations[i] >= (i+1):
            if citations[i] >= gap:
                answer = i+1
                
    return answer
