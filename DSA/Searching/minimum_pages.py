'''Allocate Minimum Number of Pages'''
# Minimize the maximum pages allocated.
# Only contiguous pages can be allocated.

# Minimum of maximum pages read by a student
arr = [10, 5, 30, 1, 2, 5, 10, 10] # Each element represents no. of pages in a book
k = 3 # Represents no. of students
n = len(arr)

def minPageRead(arr, n, k):
    if n == 1:
        return arr[0]
    if k == 1:
        return sum(arr[0: n])
    
    res = float("inf")
    for i in range(1, n):
        res = min(res, max(minPageRead(arr, i, k-1), sum(arr[i:n])))
    
    return res

def binaryMinPage(arr, k):
    total = sum(arr)
    mx = max(arr)
    low, high = mx, total
    result = 0
    # Using the range of max value and sum of the array
    while low <= high:
        mid = (low + high) // 2
        # If true, we are updating result and reducing the range
        # By updating the value of high, cause our result will not be higher than the new high
        # By same logic, result will not be lower than the new low
        if isValid(arr, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def isValid(arr, k, res):
    '''Checks if current low and high range, satisfies all the conditions'''
    # target represents a counter which is later compared with k for validity
    target = 1
    # changes to target depends of total, in case threshold is crossed
    total = 0
    for i in range(n):
        # Keep adding to the total until its higher than result
        if total + arr[i] <= res:
            total += arr[i]
        else:
            # When total higher than result we increase target and reset total
            target += 1
            total = arr[i]
    return k >= target

print(minPageRead(arr, n, k))
print(binaryMinPage(arr, k))
