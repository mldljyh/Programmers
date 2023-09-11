enter = []
max_count = 0
def dun(k, dungeons, count):
    global enter, max_count
    cannot = True
    if count == 0:
        for i in range(len(dungeons)):
            enter.append(0)
        for i in range(len(dungeons)):
            if k >= dungeons[i][0]:
                enter[i] = 1
                cannot = False
                dun(k-dungeons[i][1], dungeons, 1)
                enter[i] = 0
    else:
        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and enter[i] == 0:
                enter[i] = 1
                cannot = False
                dun(k-dungeons[i][1], dungeons, count + 1)
                enter[i] = 0
    if cannot:
        if max_count < count:
            max_count = count
                
def solution(k, dungeons):
    dun(k, dungeons, 0)
    return max_count
