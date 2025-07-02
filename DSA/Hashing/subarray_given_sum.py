"""Subarray with Given Sum"""
# There are no negative elements in the array
array = [1, 4, 20, 3, 10, 5]
total = 33


def given_sum_naive(arr, value):
    calc = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            calc += arr[j]
            if calc == value:
                return True
            elif calc > value:
                continue
        calc = 0
    return False


def given_sum_window_sliding(arr, value):
    """We are using window sliding technique with a window of variable size"""
    left, right, calc = 0, 0, 0
    while left <= right < len(arr):
        if calc == value:
            return True
        elif calc < value:
            calc += arr[right]
            right += 1
        else:
            calc -= arr[left]
            left += 1
    return False


print(given_sum_naive(array, total))
print(given_sum_window_sliding(array, total))
