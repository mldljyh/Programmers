def solution(sizes):
    max_w = max(max(size) for size in sizes)
    max_h = max(min(size) for size in sizes)
    return max_w * max_h
