"""Longest common subarray with given sum"""


def longest_common_span_naive(arr1, arr2):
    result = 0
    n = len(arr1)
    for i in range(n):
        total1 = 0
        total2 = 0
        for j in range(i, n):
            total1 += arr1[j]
            total2 += arr2[j]
            if total1 == total2:
                result = max(result, j - i + 1)
    return result


def longest_common_span_hash(arr1, arr2):
    n = len(arr1)
    hash_map = {}
    pre_sum = 0
    length = 0
    for i in range(len(arr1)):
        pre_sum += arr1[i] - arr2[i]
        if pre_sum == 0:
            length = i + 1
        if pre_sum in hash_map:
            length = max(length, i - hash_map[pre_sum])
        else:
            hash_map[pre_sum] = i
        print(hash_map, length)
    return length


array1 = [0, 1, 0, 0, 0, 0]
array2 = [1, 0, 1, 0, 0, 1]

print(longest_common_span_naive(array1, array2))
print(longest_common_span_hash(array1, array2))
