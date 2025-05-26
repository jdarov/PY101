print(True)
print(False)

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string

print(make_longer('abc', True))
print(make_longer('xyz', False))

def is_digit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False
    
print(is_digit('5'))
print(is_digit('a'))

value = True

if value is True:
    print("It's True!")
elif value is False:
    print("It's false!")
else:
    print("It's not true or false!")


name = input('Enter your name here: ')
if name:
    print(f"You typed your name, congratulations {name}!")
else:
    print('Please type a name next time')