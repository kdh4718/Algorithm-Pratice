def solution(sizes):
    height, width = 0, 0
    
    for size in sizes:
        height = max(height, max(size))
        width = max(width, min(size))
    
    return height*width