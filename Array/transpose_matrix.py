'''Transpose of Matrix'''
array = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

def naive_transpose_matrix(arr):
    i, j = 0, 0
    n = len(arr)
    temp = [[] for _ in range(n)]
    while i < n:
        while j < n:
            temp[j].append(arr[i][j])
            j += 1
        j = 0
        i += 1
    arr[:] = temp
    return temp

def effi_transpose_matrix(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

effi_transpose_matrix(array)
print(array)

