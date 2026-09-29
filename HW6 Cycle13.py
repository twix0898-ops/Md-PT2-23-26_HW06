text = input("Введите строку: ")
words = text.split()
count = 0

for word in words:
    count += 1

print("Количество слов:", count)