import math

arr = [12, 35, 1, 10, 34, 1]

highest = arr[0]
second = highest

for i in range(1, len(arr)):
    if arr[i] > highest:
        highest, second = arr[i], highest
    if second < arr[i] < highest:
        second = arr[i]

print(second)