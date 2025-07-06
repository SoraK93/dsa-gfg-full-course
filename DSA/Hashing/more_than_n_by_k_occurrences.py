"""More than n/k occurrences"""
# Get all the elements that occur more than len(arr) / k times
from collections import Counter


def n_by_k_occurrence(arr, k_value):
    count_elements = Counter(arr)
    occurrence_count = len(arr) // k_value
    for key, value in count_elements.items():
        if value > occurrence_count:
            print(key, end=" ")


def n_by_k_occurrence_naive(arr, k_value):
    arr.sort()
    count = 1
    i = 1
    while i < len(arr):
        while i < len(arr) and arr[i] == arr[i - 1]:
            count += 1
            i += 1
        if (len(arr) // k_value) < count:
            print(arr[i - 1], end=" ")
        count = 1
        i += 1


def n_by_k_occurrence_effi(arr, k_value):



array = [30, 10, 20, 20, 10, 20, 30, 30]
k = 4
n_by_k_occurrence(array, k)
print()
n_by_k_occurrence_naive(array, k)
