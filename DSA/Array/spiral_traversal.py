'''Visit each element of the matrix and print them in spiral order'''
array = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

def spiral(arr):
    top, right, bottom, left = 0, len(arr[0]) - 1, len(arr) - 1, 0

    # If our input only contain row array
    if len(arr) == 1:
        for i in range(len(arr[0])):
            print(arr[0][i])
    # If our input only contains column array
    elif len(arr[0]) == 1:
        for i in range(len(arr)):
            print(arr[i][0])
    else:
        # Using 4 variables we are maintaining our traversal path
        while top <= bottom and left <= right:
            # top
            for i in range(top, right + 1):
                print(arr[top][i], end=" ")
            top += 1
            print()
            # right
            for i in range(top, bottom + 1):
                print(arr[i][right], end=" ")
            right -= 1
            print()
            # bottom
            for i in range(right, left - 1, -1):
                print(arr[bottom][i], end=" ")
            bottom -= 1
            print()
            # left
            for i in range(bottom, top - 1, -1):
                print(arr[i][left], end=" ")
            left += 1
            print()
        
spiral(array)

# Simulation Approach
def spiral_simulation(arr):
    ans = []
    if len(arr) == 0:
        return ans
    
    len_row, len_col = len(arr), len(arr[0])
    checked_index = [[0 for i in range(len_col)] for i in range(len_row)]
    direction_row = [0, 1, 0, -1]
    direction_col = [1, 0, -1, 0]
    row, col, direction_index = 0, 0, 0

    for i in range(len_row * len_col):
        ans.append(arr[row][col])
        checked_index[row][col] = True
        curr_row = row + direction_row[direction_index]
        curr_col = col + direction_col[direction_index]

        if (0 <= curr_row and curr_row < row\
             and 0 <= curr_col and curr_col < col\
                  and not checked_index[curr_row][curr_col]):
            row = curr_row
            col = curr_col
        else:
            direction_index = (direction_index + 1) % 4
            row += direction_row[direction_index]
            col += direction_col[direction_index]
        
    return ans

