"""Longest Subarray with equal number of zero and one"""


def equal_subarray_zero_one_naive(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        count_of_1 = 0
        count_of_0 = 0
        for j in range(i, n):
            if arr[j] == 1:
                count_of_1 += 1
            else:
                count_of_0 += 1
            if count_of_0 == count_of_1:
                result = max(result, j - i + 1)
    return result


def equal_subarray_zero_one_effi(arr):
    count_of_0 = 0
    count_of_1 = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count_of_1 += 1
        else:
            count_of_0 += 1
    return min(count_of_1, count_of_0) * 2


def equal_subarray_zero_one_effi_alt(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1

    pre_sum = 0
    pre_sum_dict = dict()
    result = 0
    for i in range(n):
        pre_sum += arr[i]
        if pre_sum == 0:
            result += 1
        if pre_sum not in pre_sum_dict:
            pre_sum_dict[pre_sum] = i
        else:
            result = max(result, i - pre_sum_dict[pre_sum])
    return result


array = [1, 0, 1, 1, 1, 0, 0]
print(equal_subarray_zero_one_naive(array))
print(equal_subarray_zero_one_effi(array))
print(equal_subarray_zero_one_effi_alt(array))
