l = [ 11, 22, 3, 4, 5, 6, 7]
l1 = [11, 22, 3, 4, 4, 4, 4, 4, 33, 44, 55]



l.extend(str("10000"))
l.append("1000")
l.remove(7)
print(l)
l.extend(l1)
print(l)

print(len(l))
print(l.count(4))