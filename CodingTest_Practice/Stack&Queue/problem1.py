def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    i = -1
    for num in arr:
        if i == -1:
            answer.append(num)
            i += 1
        elif answer[i] != num:
            answer.append(num)
            i += 1
    return answer
