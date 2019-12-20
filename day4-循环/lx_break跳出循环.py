

i = 0

while i <= 10:
    #print(i)
    if i == 3:
        break
    i += 1


i = 0
sum = 0
while i <= 10:
    if i % 3 != 0:
        print(i)
       #continue
        sum += i
    i += 1
print(sum)