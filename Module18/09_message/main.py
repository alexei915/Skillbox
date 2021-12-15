import re

message = input('Сообщение: ')
new_message = []

result = re.split(r'([ ,.?!:;"()-])', message)

for i in range(len(result)):
    new_message.append(result[i][::-1])

new_message = ''.join(new_message)

print(new_message)
