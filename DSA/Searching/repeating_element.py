'''Repeating Element'''
# Numbers in the array will always be greater than zero
# Only one element in the array will get repeated multiple times
arr = [0, 2, 1, 3, 5, 4, 6, 2]
arr_noZero = [1, 3, 2, 4, 6, 5, 7, 3]


# Nested Loop Method
def loop_findRepeat(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return arr[i]
    return -1

# Sorting Method
def sort_findRepeat(arr):
    arrSort = sorted(arr)
    for i in range(1, len(arrSort)):
        if arrSort[i - 1] == arrSort[i]:
            return arrSort[i]
    return -1

# Array Bit Method
def bit_findRepeat(arr):
    n = len(arr)
    tempArr = [0] * n
    for i in arr:
        if tempArr[i] == 1:
            return i
        tempArr[i] = 1
    return -1

# Slow Fast Pointer Method
# Array does not include zero [1, 3, 2, 4, 6, 5, 7, 3]
def twoPointer_findRepeat_noZero(arr):
    slow = arr[0]
    fast = arr[0]
    slow = arr[slow]
    fast = arr[arr[fast]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow
# Array does include zero [0, 2, 1, 3, 5, 4, 6, 2]
def twoPointer_findRepeat_withZero(arr):
    slow = arr[0] + 1
    fast = arr[0] + 1
    slow = arr[slow] + 1
    fast = arr[arr[fast] + 1] + 1
    while slow != fast:
        slow = arr[slow] + 1
        fast = arr[arr[fast] + 1] + 1
    slow = arr[0] + 1
    while slow != fast:
        slow = arr[slow] + 1
        fast = arr[fast] + 1
    return slow - 1

# Hashing Method
def hash_findRepeat(arr):
    n = len(arr)
    hashValue = set()
    for ele in arr:
        if ele in hashValue:
            return ele
        hashValue.add(ele)
    return -1

print(loop_findRepeat(arr))
print(sort_findRepeat(arr))
print(bit_findRepeat(arr))
print(twoPointer_findRepeat_noZero(arr_noZero))
print(twoPointer_findRepeat_withZero(arr))
print(hash_findRepeat(arr))
