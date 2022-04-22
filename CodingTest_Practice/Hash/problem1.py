# Programmers Coding Test Practice Hash Problem 1
# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    name = dict.fromkeys(participant,0)
    for i in participant:
        name[i] = name[i] + 1
    for i in completion:
        name[i] = name[i] - 1
        if name[i] == 0:
            name.pop(i)
    answer = list(name.keys())[0]
    return answer
