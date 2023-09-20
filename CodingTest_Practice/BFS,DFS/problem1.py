counter = 0
def recur(numbers, now, target, count):
    global counter
    #print(counter, now, count)
    if count == len(numbers):
        if now == target:
            counter += 1
        return
    num = numbers[count]
    recur(numbers, now + num, target, count+1)
    recur(numbers, now - num, target, count+1)

def solution(numbers, target):
    recur(numbers, 0, target, 0)
    return counter
