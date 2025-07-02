arr = [5, 3, 8]

def minDiff(arr):
    res = float("inf")
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            res = min(res, abs(arr[i] - arr[j]))
    return res

def sort_minDiff(arr):
    if len(arr) <= 1:
        return float("inf")
    array = arr[::]
    array.sort()
    res = float("inf")
    for i in range(1, len(array)):
        res = min(res, array[i]-array[i-1])
    return res

print(minDiff(arr))
print(sort_minDiff(arr))
