def solution(progresses, speeds):
    answer = []
    max = 0
    for i in range(0, len(progresses)):
        if ((100 - progresses[i])/speeds[i]) - int(((100 - progresses[i])/speeds[i])) > 0: 
            progress_time = int((100 - progresses[i])/speeds[i]) + 1
        else:
            progress_time = int((100 - progresses[i])/speeds[i])
        if max == 0:
            max = progress_time
            answer.append(1)
        elif max >= progress_time:
            answer[-1] += 1
        else:
            max = progress_time
            answer.append(1)
    return answer
