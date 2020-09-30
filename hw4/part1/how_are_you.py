#! python3
'''
examples of upper(), lower(), isupper(), and 
islower() string methods
'''

spam = 'Hello world!'

spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')