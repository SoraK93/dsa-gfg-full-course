'''Rotate a Matrix by 90deg'''
array = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

# Naive Solution
def naive_rotate_matrix(arr):
    n = len(arr)
    temp = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-j-1].append(arr[i][j])
    arr[:] = temp

def effi_rotate_matrix(arr):
    n = len(arr)
    # transpose
    for i in range(n):
        for j in range(i+1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # reverse newly transposed array
    for i in range(n // 2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

# naive_rotate_matrix(array)
effi_rotate_matrix(array)
print(array)
