count = 0
enter = []
def wire_count(cut_wires, start):
    global count, enter
    for i in range(len(cut_wires)):
        if cut_wires[i][0] == start and not cut_wires[i][1] in enter:
            count += 1
            enter.append(cut_wires[i][1])
            wire_count(cut_wires[:i] + cut_wires[i+1:], cut_wires[i][1])
        if cut_wires[i][1] == start and not cut_wires[i][0] in enter:
            count += 1
            enter.append(cut_wires[i][0])
            wire_count(cut_wires[:i] + cut_wires[i+1:], cut_wires[i][0])
def solution(n, wires):
    global count, enter
    answer = n
    wires.sort()
    for i in range(len(wires)):
        count = 1
        cut_wires = wires[:i] + wires[i+1:]
        enter = [1]
        wire_count(cut_wires, 1)
        result = count * 2 - n
        if result < 0:
            result = -result
        if answer > result:
            answer = result
    return answer
