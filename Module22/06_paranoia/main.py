def code(text):
    encoded_string = ''
    for sym in text:
        if sym.lower() in alphabet:
            if sym.isupper():
                encoded_string += alphabet[(alphabet.index(sym.lower()) + shift) % len(alphabet)].upper()
            else:
                encoded_string += alphabet[(alphabet.index(sym) + shift) % len(alphabet)]
        else:
            encoded_string += sym
    return encoded_string


alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 1
amount_str = ''


file = open('text.txt', 'r', encoding='utf-8')
new_file = open('cipher_text.txt', 'w')

print('Содержимое файла text.txt:')
for i_line in file:
    print(i_line, end='')
    amount_str += code(i_line)
    shift += 1

new_file.write(amount_str)
file.close()
new_file.close()

new_file = open('cipher_text.txt', 'r', encoding='utf-8')

print('\n\nСодержимое файла cipher_text.txt:')
for line in new_file:
    print(line, end='')

new_file.close()
