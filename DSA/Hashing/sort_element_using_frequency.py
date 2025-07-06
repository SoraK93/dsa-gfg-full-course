"""Sort Elements by Decreasing Frequency"""
# Given an array of integers arr[], sort the array according to the frequency of elements,
# i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same,
# then the smaller number comes first.
from collections import Counter


def sort_by_freq(arr):
    freq_count = Counter(arr)
    freq_list = sorted(freq_count.items(), key=lambda x: (-x[1], x[0]))
    ans = []
    for ele, freq in freq_list:
        ans.extend([ele] * freq)
    return ans


def sort_by_freq_alt(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))
