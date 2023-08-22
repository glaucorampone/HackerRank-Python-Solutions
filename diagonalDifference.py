def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    left_to_right = 0
    right_to_left = 0
    for i in range(n):
        left_to_right += arr[i][i]
        right_to_left += arr[i][n-i-1]
    result = abs(left_to_right - right_to_left)
    return result
