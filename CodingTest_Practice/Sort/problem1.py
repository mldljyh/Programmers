def solution(array, commands):
    answer = []
    for start, end, select in commands:
        answer.append(sorted(array[start-1:end])[select-1])
    return answer
