# Programmers Coding Test Practice Hash Problem 2
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(0,len(phone_book)-1):
        if(len(phone_book[i]) < len(phone_book[i+1])):
            if(phone_book[i+1].startswith(phone_book[i])):
                answer = False
                break
    return answer
