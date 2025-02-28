'''
A sequence x1, x2, ..., xn is Fibonacci-like if:
    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
'''

# Wrong solution. Solves different problem.
def lenLongestFibSeq(arr: list[int]) -> int:
    longestFromN = [0] * len(arr)
    max_yet = 0
    for i in reversed(range(len(arr)-2)):
        if arr[i+2] == arr[i+1] + arr[i]:
            longestFromN[i] = 3 if longestFromN[i+1] == 0 else longestFromN[i+1]+1
            if longestFromN[i] > max_yet:
                max_yet = longestFromN[i]
    print(longestFromN)
    return 0 if max_yet < 3 else max_yet
"""
print(lenLongestFibSeq([1, 2, 3, 4]))
print(lenLongestFibSeq([1,2,3,4,5,6,7,8]))
"""

## Prob using smth like a matrix? First dimension is best starting from n. Second dimension is best starting from n second m. O(N^3) XD
def lenLongestFibSubseq(arr: list[int]) -> int:
    longestStartingNSecondM = [[0]*len(arr) for _ in arr]
    max_yet = 0
    for row in reversed(range(len(arr)-2)):
        for col in reversed(range(row+1, len(arr)-1)):
            # Checking if there exists a number in the array that is equal to the sum of arr[row] and arr[col]
            fibContinuation = None
            for numIdx in range(col+1, len(arr)):
                if arr[numIdx] > arr[row]+arr[col]:
                    break
                elif arr[numIdx] == arr[row]+arr[col]:
                    fibContinuation = numIdx
                    break
            # If it exists, then the longest subseq starting in arr[row] with second elem arr[col]...
            if fibContinuation:
                longestStartingNSecondM[row][col] = 3 if longestStartingNSecondM[col][fibContinuation] == 0 else longestStartingNSecondM[col][fibContinuation] + 1
                # Update if it is the biggest yet
                if longestStartingNSecondM[row][col] > max_yet:
                    max_yet = longestStartingNSecondM[row][col]
    print(longestStartingNSecondM)
    return max_yet

print(lenLongestFibSubseq([1, 2, 3, 4]))
print(lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(lenLongestFibSubseq([1,3,7,11,12,14,18]))

# Qué hueva. Para buscar los elementos era mejor solo hacer un set. Reduce a O n^2
def lenLongestFibSubseq(arr: list[int]) -> int:
    longestStartingNSecondM = [[0]*len(arr) for _ in arr]
    numbersInArr = {num: index for index, num in enumerate(arr)}
    max_yet = 0
    for row in reversed(range(len(arr)-2)):
        for col in reversed(range(row+1, len(arr)-1)):
            # Checking if there exists a number in the array that is equal to the sum of arr[row] and arr[col]
            fibContinuation = numbersInArr.get(arr[row]+arr[col], None)
            # If it exists, then the longest subseq starting in arr[row] with second elem arr[col]...
            if fibContinuation:
                longestStartingNSecondM[row][col] = 3 if longestStartingNSecondM[col][fibContinuation] == 0 else longestStartingNSecondM[col][fibContinuation] + 1
                # Update if it is the biggest yet
                if longestStartingNSecondM[row][col] > max_yet:
                    max_yet = longestStartingNSecondM[row][col]
    print(longestStartingNSecondM)
    return max_yet      
print(lenLongestFibSubseq([1, 2, 3, 4]))
print(lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(lenLongestFibSubseq([1,3,7,11,12,14,18]))
