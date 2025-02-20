
def maximalSquare(matrix: list[list[str]]) -> int:
    max_sq_topleft = [[-1 for column in row] for row in matrix]
    #maximalSquareRec(matrix, 0, 0, max_sq_topleft)
    maximalSquareIt(matrix, max_sq_topleft)
    return pow(max([max(row) for row in max_sq_topleft]), 2)
        
def maximalSquareRec(matrix: list[list[str]], row_pos: tuple, col_pos: tuple, max_matrix):
    bottom, right, diagonal = 0, 0, 0
    if row_pos+1 != len(matrix):
        if max_matrix[row_pos+1][col_pos] == -1: 
            maximalSquareRec(matrix, row_pos+1, col_pos, max_matrix)
        bottom = max_matrix[row_pos+1][col_pos]
    if col_pos+1 != len(matrix[0]):
        if max_matrix[row_pos][col_pos+1] == -1: 
            maximalSquareRec(matrix, row_pos, col_pos+1, max_matrix)
        right = max_matrix[row_pos][col_pos+1]
    if row_pos+1 != len(matrix) and col_pos+1 != len(matrix[0]):
        if max_matrix[row_pos+1][col_pos+1] == -1: 
            maximalSquareRec(matrix, row_pos+1, col_pos+1, max_matrix)
        diagonal = max_matrix[row_pos+1][col_pos+1]
    if matrix[row_pos][col_pos] == '0':
        # The cell is not zero.
        max_matrix[row_pos][col_pos] = 0
    else:
        max_matrix[row_pos][col_pos] = 1 + min(bottom, right, diagonal)

def maximalSquareIt(matrix: list[list[str]], max_matrix):
    for row_i in reversed(range(len(matrix))):
        for col_i in reversed(range(len(matrix[row_i]))):
            if matrix[row_i][col_i] == '0':
                # The cell is not zero.
                max_matrix[row_i][col_i] = 0
                continue
            bottom, right, diagonal = 0, 0, 0
            if row_i+1 != len(matrix):
                bottom = max_matrix[row_i+1][col_i]
            if col_i+1 != len(matrix[row_i]):
                right = max_matrix[row_i][col_i+1]
            if row_i+1 != len(matrix) and col_i+1 != len(matrix[row_i]):
                diagonal = max_matrix[row_i+1][col_i+1]
            max_matrix[row_i][col_i] = 1 + min(bottom, right, diagonal)


print(maximalSquare([["1","0","1","0","0"],
                         ["1","0","1","1","1"],
                         ["1","1","1","1","1"],
                         ["1","0","0","1","0"]]))
print(maximalSquare([["0","1"]]))
print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))