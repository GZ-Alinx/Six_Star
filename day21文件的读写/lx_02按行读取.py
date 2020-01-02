f = open('1.txt', 'r+', encoding='UTF-8')

while True:
    text = f.readline()

    if not text:
        break
    print(text)

f.close()