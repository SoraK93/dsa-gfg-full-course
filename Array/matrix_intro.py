'''Matrix = A list of lists'''

# Matrix Traversal
def traversal_basic(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

# Matrix Traversal - Alternate
def traversal_alt(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()
    
# Create Matrix
def create_arr(col, row):
    # Do not use multiplication method to create matrix, reference to each elements will be bugged
    # XX array = [[[0] * col] * row] XX NOT RECOMMENDED!!
    array = [[0 for _ in range(col)] for _ in range(row)]
    return array

arr = create_arr(3,3)
print(arr)
traversal_basic(arr)
traversal_alt(arr)
