#헷갈려서 인터넷에서 찾아가면서 푼 문제
def solution(number, k):
    stack = []
    for num in number:
        #print(stack)
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)
    #print(stack)
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack)

