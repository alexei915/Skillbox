word = input('Введите слово: ')
symbol = list(word)
palindrome = True

for i in range(1, len(symbol)//2 + 1):
    if symbol[i - 1] != symbol[-i]:
        print('Слово не является палиндромом.')
        palindrome = False
        break

if palindrome:
    print('Слово является палиндромом.')
