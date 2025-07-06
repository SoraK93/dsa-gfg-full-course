def freq(arr):
    count = dict()
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count


array = [10, 20, 20, 30, 10]
cnt = freq(array)
for key, value in cnt.items():
    print(key, value)
