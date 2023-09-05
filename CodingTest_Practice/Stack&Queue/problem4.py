def solution(priorities, location): 
    last_max_i = -1
    count = 0
    while len(priorities) > 0:
        count += 1
        max = priorities[0]
        max_i = 0
        trigger = True
        for i in range(1, len(priorities)):
            if priorities[i] != -1:
                if max < priorities[i]:
                    max = priorities[i]
                    max_i = i
                    trigger = True
                elif max == priorities[i] and (last_max_i > max_i and last_max_i < i):
                    max = priorities[i]
                    max_i = i
                    trigger = False
        priorities[max_i] = -1 
        print(priorities)
        if trigger:
            last_max_i = max_i
        if max_i == location:
            return count
    return 0
