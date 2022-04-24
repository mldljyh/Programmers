# Programmers Coding Test Practice Hash Problem 3
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    kinds = {}
    for i in range(0, len(clothes)):
        if clothes[i][1] in kinds:
            kinds[clothes[i][1]] = kinds[clothes[i][1]] + 1
        else:
            kinds[clothes[i][1]] = 1
    for i in kinds:
        answer = answer * (kinds[i] + 1)
    answer = answer - 1
    return answer
