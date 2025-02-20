def largestRectangleArea(heights: list[int]) -> int:
    # Max rectangle that ends in the ith position and has j+1 height.
    max_rectangle = [[0]*max(heights) for height in heights]
    max_yet = 0
    for i, height in enumerate(heights):
        # Again. What we want to do is count from 1 to height, but the array is made from 0 to h-1. 
        for h in range(height):
            max_rectangle[i][h] = h+1 if i == 0 else max_rectangle[i-1][h] + (h+1)
            if max_rectangle[i][h] > max_yet: 
                max_yet = max_rectangle[i][h]
    return max_yet

def largestRectangleArea2(heights: list[int]) -> int:
    if max(heights) == 0: return 0
    max_yet = 0
    # Initialize first rectangle
    max_rectangle = [0]*max(heights)
    for height in heights: 
        max_rectangle = [max_rectangle[h] + (h+1) if h < height else 0 for h in range(len(max_rectangle))]
        if max(max_rectangle) > max_yet: max_yet = max(max_rectangle)
    return max_yet

def largestRectangleArea3(heights: list[int]) -> int:
    max_yet = 0
    # Initialize first rectangle
    max_rectangle = []
    for height in heights: 
        max_rectangle = [max_rectangle[h] + (h+1) if h < len(max_rectangle) else h+1 for h in range(height)]
        if len(max_rectangle) > 0 and max(max_rectangle) > max_yet: max_yet = max(max_rectangle)
    return max_yet


print(largestRectangleArea([1, 2, 3, 4]))
print(largestRectangleArea3([1, 2, 3, 4]))

print(largestRectangleArea([2,4]))
print(largestRectangleArea3([2,4]))

print(largestRectangleArea([0]))
print(largestRectangleArea3([0]))

print(largestRectangleArea([0, 9]))
print(largestRectangleArea3([0, 9]))

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea3([2,1,5,6,2,3]))