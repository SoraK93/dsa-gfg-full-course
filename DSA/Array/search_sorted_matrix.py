array = [[10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
x = 29

def naive_search(matrix, k):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == k:
                return i, j
    return "Not Found"

def effi_search(matrix, k):
    top, right = 0, len(matrix[0]) - 1
    while top < len(matrix) and right >= 0:
        if matrix[top][right] == k:
            return top, right
        elif matrix[top][right] > k:
            right -= 1
        else:
            top += 1
    return "Not Found"

print(f"Index of {x}: {naive_search(array, x)}")
print(f"Index of {x}: {effi_search(array, x)}")
