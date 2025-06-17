def isArraySorted(arr):
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and isArraySorted(arr[1:])

A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
print(isArraySorted(A))