"""Pair with given sum in Unsorted Array"""
from DSA.Sorting import quick_sort
from DSA.Searching import binary_search

array = [3, 2, 8, 15, -8]
value = 17


def pair_with_sum_naive(arr, total):
    """Nested loop Approach"""
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == total:
                return True
    return False


def pair_with_sum_hash(arr, total):
    """Hashing Approach"""
    union_set = set()
    for num in arr:
        if total - num in union_set:
            return True
        union_set.add(num)
    return False


def pair_with_sum_sort(arr, total):
    """Sorting Approach"""
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


def pair_with_sum_binary(arr, total):
    """Binary Search Approach"""
    n = len(arr)
    low = 0
    high = n - 1
    quick_sort(arr, low, high)

    i = 0
    while i < n - 1:
        if binary_search(arr, total - arr[i]) != -1:
            return True
        i += 1

    return False


print(pair_with_sum_naive(array, value))
print(pair_with_sum_hash(array, value))
print(pair_with_sum_sort(array, value))
print(pair_with_sum_binary(array, value))
