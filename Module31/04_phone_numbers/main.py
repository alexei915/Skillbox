import re


phone_numbers = ['9999999999', '999999-999', '99999x9999', '75554448965', '8111222548', '9465468590']

pattern = r'\b[8,9]\d{9}\b'

for i_number in range(len(phone_numbers)):
    if re.search(pattern, phone_numbers[i_number]):
        print('{}-й номер: подходит'.format(i_number + 1))
    else:
        print('{}-й номер: не подходит'.format(i_number + 1))