from lomuto_quickSort import lomuto

arr = [30, 20, 5, 10, 8]
k = 4

def kth_smallest(arr, k):
    arr.sort()
    return arr[k]

def quickSelect(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        p = lomuto(arr, low, high)
        if p == k:
            return arr[p]
        elif p > k:
            high = p - 1
        else:
            low = p + 1
    return -1

print(kth_smallest(arr, k))
print(quickSelect(arr, k))