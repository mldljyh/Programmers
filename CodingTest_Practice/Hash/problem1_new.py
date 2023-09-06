def solution(nums):
    answer = 0
    pokes = {}
    for i in nums:
        if not i in pokes:
            pokes[i] = '1'
    if len(pokes) > int(len(nums)/2):
        answer = int(len(nums)/2)
    else:
        answer = len(pokes)
    return answer
