"""Given an array of positive and negative numbers, find if there is a subarray (of size at least one) with zero-sum"""
array = [4, 3, -2, 1, 1]


def is_zero_sum_naive(arr):
    """Using nested loop to iterate through and find """
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(arr[i:j]) == 0:
                return True
    return False


def is_zero_sum_hash(arr):
    """Stores pre-sum by iterating through the array and storing calculated sum in hashset"""
    pre_sum_set = set()
    pre_sum = 0
    for i in range(len(arr)):
        pre_sum += arr[i]
        if pre_sum == 0 or pre_sum in pre_sum_set:
            return True
        pre_sum_set.add(pre_sum)
    return False


print(is_zero_sum_naive(array))
print(is_zero_sum_hash(array))
