min_count = int(1e9)
visit = []
def move(word_count, count, num, current):
    global min_count, visit
    if len(visit) == 0:
        if min_count > count:
            min_count = count
    else:
        if current > len(visit) - 1:
            after = 0
        else:
            after = current
        if current - 1 >= 0:
            before = current - 1
        else:
            before = len(visit) - 1

        now = visit.pop(before)
        if num < now:
            add_num = now - num
            move(word_count, count + word_count[now] + add_num, now, before)
            add_num = len(word_count) - now + num
            move(word_count, count + word_count[now] + add_num, now, before)
        else:
            add_num = num - now
            move(word_count, count + word_count[now] + add_num, now, before)
            add_num = len(word_count) - num + now
            move(word_count, count + word_count[now] + add_num, now, before)
        visit.insert(before, now)
        now = visit.pop(after)
        if num < now:
            add_num = now - num
            move(word_count, count + word_count[now] + add_num, now, after)
            add_num = len(word_count) - now + num
            move(word_count, count + word_count[now] + add_num, now, after)
        else:
            add_num = num - now
            move(word_count, count + word_count[now] + add_num, now, after)
            add_num = len(word_count) - num + now
            move(word_count, count + word_count[now] + add_num, now, after)
        visit.insert(after, now)
        
def solution(name):
    global visit
    word = []
    word_count = []
    check = False
    for i in range(len(name)):
        word.append('A')
        word_count.append(0)
    if ord(name[0]) - ord('A') < ord('Z')- ord(name[0]) + 1:
        word_count[0] = int(ord(name[0]) - ord('A'))
    else:
        word_count[0] = int(ord('Z') - ord(name[0]) +1)
    for i in range(1, len(name)):
        if name[i] != 'A':
            if ord(name[i]) - ord('A') < ord('Z')- ord(name[i]) + 1:
                word_count[i] = int(ord(name[i]) - ord('A'))
                visit.append(i)
            else:
                word_count[i] = int(ord('Z') - ord(name[i]) +1)
                visit.append(i)
        
    move(word_count, word_count[0], 0, 0)
    return min_count

