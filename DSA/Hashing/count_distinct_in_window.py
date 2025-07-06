"""Count distinct elements in every window"""
from collections import Counter


def count_distinct_elements_naive(arr, k):
    result = 0
    for i in range(len(arr) - k + 1):
        result = max(result, len(set(arr[i:i+k])))
    return result


def count_distinct_elements_dict(arr, k):
    window = Counter(arr[0:k])
    result = len(window)
    for i in range(k, len(arr)):
        prev_window_start = arr[i - k]
        curr_window_end = arr[i]

        window[prev_window_start] -= 1
        window[curr_window_end] += 1

        if window[prev_window_start] == 0:
            del window[prev_window_start]
        result = max(result, len(window))

    return result


array = [10, 20, 20, 10, 30, 40, 10]
window_size = 4
print(count_distinct_elements_naive(array, window_size))
print(count_distinct_elements_dict(array, window_size))

print(((90 % 23) + 1 + (90 % 19)) % 23)
