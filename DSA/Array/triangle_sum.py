def sumTriangles(matrix, n):
    # code here 
    upper, lower = 0, 0
    len_row, len_col = len(matrix), len(matrix[0])
    
    for row_index in range(len_row):
        for upper_index in range(row_index, len_col):
            upper += matrix[row_index][upper_index]
        for lower_index in range(0, row_index + 1):
            lower += matrix[row_index][lower_index]
    
    return [upper, lower]