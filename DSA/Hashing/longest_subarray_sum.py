"""Longest Subarray with given sum"""
# Given an array arr[] of size n containing integers.
# The problem is to find the length of the longest sub-array having sum equal to the given value k.


def longest_subarray_sum_naive(arr, value):
    """Using nested loops to find out the length of longest subarray"""
    n = len(arr)
    result = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == value:
                result = max(result, j-i+1)
    return result


def longest_subarray_sum_dict(arr, value):
    n = len(arr)
    my_dict = dict()
    pre_sum = 0
    result = 0
    for i in range(n):
        pre_sum += arr[i]
        if pre_sum == value:
            result = i + 1
        if pre_sum not in my_dict:
            my_dict[pre_sum] = i
        if pre_sum - value in my_dict:
            result = max(result, i - my_dict[pre_sum - value])
    return result


array = [5, 8, -4, -4, 9, -2, 2]
total = 0
print(longest_subarray_sum_naive(array, total))
print(longest_subarray_sum_dict(array, total))
