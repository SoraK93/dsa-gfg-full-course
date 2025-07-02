'''Pair with given sum in Unsorted Array'''
from DSA.Sorting import quick_sort

arr = [3, 2, 8, 15, -8]
total = 17

def pair_with_sum_naive(arr, total):
    '''Nested loop Approach'''
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == total:
                return True
    return False

def pair_with_sum_hash(arr, total):
    '''Hashing Approach'''
    union_set = set()
    for num in arr:
        if total - num in union_set:
            return True
        union_set.add(num)
    return False

def pair_with_sum_sort(arr, total):
    '''Sorting Approach'''
    low = 0
    high = len(arr) - 1
    quick_sort(arr, low, high)
    while low <= high:
        calc_total = arr[low] + arr[high]
        if calc_total == total:
            return True
        elif calc_total < total:
            low += 1
        else:
            high -= 1
    return False

print(pair_with_sum_naive(arr, total))
print(pair_with_sum_hash(arr, total))
print(pair_with_sum_sort(arr, total))
