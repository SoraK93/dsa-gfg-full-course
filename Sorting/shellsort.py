def shellsort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(arr, startposition, sublistcount)
        
        print(f"After increments of size {sublistcount}. This list is {arr}")
        sublistcount = sublistcount // 2

def gapInsertionSort(arr, start, gap):
    for i in range(start+gap, len(A), gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position -= gap
        
        arr[position] = currentvalue

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
shellsort(A)
print(A)