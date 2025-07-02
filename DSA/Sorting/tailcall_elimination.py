from quicksort import partition_index

def quickSort(arr, l, r):
    while l < r:
        p = partition_index(arr, l, r)
        quickSort(arr, l, p)
        l = p+1

if __name__ == "__main__":
    arr = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    quickSort(arr, 0, len(arr)-1)
    print(arr)