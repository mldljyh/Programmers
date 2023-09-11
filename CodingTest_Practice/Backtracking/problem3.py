def solution(answers):
    answer = []
    count = []
    for i in range(0,len(answers)):
        count.append(0)
    first = 1
    second = 1
    num = 0
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(0,len(answers)):
        if first == answers[i]:
            count[0] += 1
        if i%2 == 0 and answers[i] == 2:
            count[1] += 1
        if i%2 == 1:
            if answers[i] == second:
                count[1] += 1
            second += 1
        if answers[i] == third[num]:
            count[2] += 1
        first += 1
        num += 1
        if first > 5:
            first = 1
        if num > 9:
            num = 0
        if second == 2:
            second += 1
        if second > 5:
            second = 1
    max_count = max(count)
    for i in range(len(count)):
        if count[i] == max_count:
            answer.append(i+1)
    return answer
