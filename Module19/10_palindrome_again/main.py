def check_palindrome(text):
    string_lower = text.lower()
    letter = dict()
    middle = 0
    for i_letter in string_lower:
        if i_letter not in letter:
            letter[i_letter] = 1
        else:
            letter[i_letter] += 1
    for i_count in letter.keys():
        if letter[i_count] % 2 != 0:
            middle += 1
    if middle > 1:
        return False
    return True


string = input('Введите строку: ')
if check_palindrome(string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

