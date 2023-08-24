def gridChallenge(grid):
    # Write your code here

    matrix = []
    for string in grid:
        matrix.append(sorted(list(string)))
    n = len(matrix[0])
    ordered = True
    for i in range(n):
        column_i = [row[i] for row in matrix]
        if column_i != sorted(column_i):
            return "NO"
    return "YES"
