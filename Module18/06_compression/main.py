text = input('Введите строку: ')

new_string = []
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    if text[i] != text[i + 1] or i == len(text) - 2:
        new_string.append(text[i])
        new_string.append(str(count))
        count = 1
if text[-1] != text[-2]:
    new_string.append(text[-1])
    new_string.append(str(1))

encoded_string = ''.join(new_string)
print(encoded_string)
