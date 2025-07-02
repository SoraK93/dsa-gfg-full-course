mat1 = [[1, 2, 3, 4], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
mat2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
res = [[1, 2, 3, 4], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


def multiplyMatrix(mat1, mat2, result):
    
    # Loops rows of mat1
    for i in range(len(mat1)):
        
        # Loops col of mat1 and mat2
        for j in range(len(mat2[i])):
            
            # Loops row of mat2
            multiple = 0
            for k in range(len(mat1[i])):
                multiple += mat1[i][k] * mat2[k][j]
                
            if result[i][j] != multiple:
                return False
    
    return True