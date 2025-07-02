'''Chocolate Distribution Problem'''
# Function return the minimum possible difference between maximum and minimum value

num_of_choco = [7, 3, 2, 4, 9, 12, 56]
child = 3

def fairDistribution(chocoList, children):
    array = chocoList[::]
    children -= 1
    array.sort()
    res = float("inf")
    for i in range(children, len(array) - children):
        res = min(res, array[i] - array[i - children])
        print(array, res, array[i], array[i - children])
    return res

print(fairDistribution(num_of_choco, child))

