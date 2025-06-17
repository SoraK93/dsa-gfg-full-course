li = [2,3,9]
li = [[x for x in [li]] for x in range(3)]
print(li)


a = ["Geeks", "for", "Geeks"]
b = [i[0].upper() for i in a]
print(b)


a = "Geeks 22536 for 445 Geeks"
b = [i for i in (int(x) for x in a if x.isdigit()) if not (i & 1)]
print(b)


a = [i for i in (x for x in "Geeks 22966 for Geeks" if x.isdigit()) if i in [x for x in range(20)]]
print(a)