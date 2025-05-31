user_name = input('What is your name? ')

if user_name[len(user_name)-1] == '!':
    print(f'HELLO {user_name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {user_name}')