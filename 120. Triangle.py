def minimumTotal(triangle: list[list[int]]) -> int:
    min_path = {}
    for i, level in reversed(list(enumerate(triangle))):
        for j in range(len(level)):
            memo = 0 if i == len(triangle)-1 else min(min_path[i+1,j], min_path[i+1,j+1])
            min_path[i,j] = triangle[i][j] + memo
    return min_path[0,0]
    
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))