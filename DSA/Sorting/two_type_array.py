'''Sort an array with two types of element'''
arr = [-13, -10, 12, 19]

def linearSort(arr):
    n = len(arr)
    temp = [0] * n
    i = 0
    for j in range(n):
        if arr[j] < 0:
            temp[i] = arr[j]
            i += 1
    
    for  j in range(n):
        if arr[j] > 0:
            temp[i] = arr[j]
            i += 1

    arr[:] = temp

def howre_quickSort(arr):
    n = len(arr)
    low = -1
    high = n
    while low <= high:
        low += 1
        while low < n and arr[low] < 0:
            low += 1
        
        high -= 1
        while high >= 0 and arr[high] > 0:
            high -= 1
        
        arr[low], arr[high] = arr[high], arr[low]
