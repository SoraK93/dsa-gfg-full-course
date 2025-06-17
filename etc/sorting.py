# Consider two arrays a=[1,2,4,5,6] and b=[2,4,4,6,8] then their union will be 1,2,4,5,6,8
def union(a, b):
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while len_a > i and len_b > j:
        if i > 0 and a[i] == a[i-1]:
            i += 1
        elif j > 0 and b[j] == b[j-1]:
            j += 1
        elif a[i] < b[j]:
            print(a[i], end=" ")
            i += 1
        elif a[i] == b[j]:
            print(a[i], end=" ")
            i += 1
            j += 1
        else:
            print(b[j], end=" ")
            j += 1
    
    while len_a > i:
        if a[i] != a[i-1]:
            print(a[i], end=" ")
        i += 1

    while len_b > j:
        if b[j] != b[j-1]:
            print(b[j], end=" ")
        j += 1

a=[1,2,4,5,6]
b=[2,4,4,6,8]
union(a, b)