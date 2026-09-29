text = input("Введите строку: ")
found = False

for char in text:
    if char == "@":
        found = True
        break

if found:
    print('Есть "@"')
else:
    print('Нет "@"')