text = input("Введите строку: ")
vowels = "a, e, i, o, u, e"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Количество гласных:", count)