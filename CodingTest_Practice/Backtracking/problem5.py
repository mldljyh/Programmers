def solution(brown, yellow):
    answer = []
    colors = brown + yellow
    for hori in range(3, colors):
        if colors/hori <= hori:
            break
    while True:
        if colors%hori == 0:
            verti = colors / hori
            side = hori * 2 + (verti - 2) * 2
            if side == brown and (colors - side) == yellow:
                answer.append(hori)
                answer.append(verti)
                break
            hori += 1
        else:
            hori += 1
    return answer
