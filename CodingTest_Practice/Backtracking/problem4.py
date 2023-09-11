used = []
same = []
num_count = 0
def source(numbers, num):
    global used, num_count, same
    if num != '' and int(num) > 1:
        can = False
        test_num = int(num)
        for i in range(2, test_num - 1):
            if test_num % i == 0:
                can = True
                break
        if can == False:
            same.append(num)
            num_count += 1
    for i in range(len(used)):
        if used[i] == 0 and not (numbers[i] == '0' and num == '') and not (num + numbers[i]) in same:
            used[i] = 1
            source(numbers, num+numbers[i])
            used[i] = 0
            
def solution(numbers):
    for i in range(len(numbers)):
        used.append(0)
    source(numbers, '')
    return num_count
