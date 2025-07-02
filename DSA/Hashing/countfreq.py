def freq(arr):
    count = dict()

    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    return count

arr = [10, 20, 20, 30, 10]

count = freq(arr)

for key, value in count.items():
    print(key, value)