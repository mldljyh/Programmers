'''
개인적으로 어려웠던 문제 어떻게 비교할지에 대한 고민을 오래했던 거 같다
'''
import math
def solution(numbers):
    answer = ''
    str_numbers = []
    for i in range(len(numbers)):
        num = str(numbers[i])
        count = len(num)
        add_count = math.ceil(4/count)
        num = num * add_count
        num = num[:4]
        str_numbers.append([num, count])
    str_numbers = list(reversed(sorted(str_numbers, key=lambda x : x[0])))
    for nums, count in str_numbers:
        answer = answer + nums[:count]
    if answer.count('0') == len(answer):
        answer = '0'
    return answer
            
