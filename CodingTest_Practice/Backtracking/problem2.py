def solution(n, lost, reserve):
    answer = 0
    have = []
    lost.sort()
    reserve.sort
    have.append(0)
    for i in range(1, n+1): have.append(1)
    i = 0
    while i < len(lost):
        have[lost[i]] = 0
        if lost[i] in reserve:
            have[lost[i]] = 1
            reserve.remove(lost[i])
            lost.remove(lost[i])
        else:
            i += 1
    for i in range(len(reserve)):
        if reserve[i] != n:
            have[reserve[i]+1] += 1
        if reserve[i] != 1:
            have[reserve[i]-1] += 1
    for i in range(len(lost)):
        if have[lost[i]] == 1:
            if i+1 < len(lost) and have[lost[i+1]] >= 1 and lost[i+1] == lost[i] + 2:
                have[lost[i+1]] -= 1
    for i in have:
        if i>0:
            answer += 1
            
        
    return answer
