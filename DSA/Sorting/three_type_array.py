arr = [0, 1, 2, 1, 0, 2]
# Naive Approach
def sortArr(arr):
    # A total of 4 traversal is required in this solution
    temp = []
    for ele in arr:
        if ele == 0:
            temp.append(ele)
    
    for ele in arr:
        if ele == 1:
            temp.append(ele)
    
    for ele in arr:
        if ele == 2:
            temp.append(ele)
    
    arr[:] = temp

sortArr(arr)
print(arr)

arr = [0, 1, 2, 1, 1, 2]
def dutchNationalAlgorithm(arr):
    # By using 3 pointers, can sort this array in single traversal
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

dutchNationalAlgorithm(arr)
print(arr)
