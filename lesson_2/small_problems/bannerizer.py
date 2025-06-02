def print_in_box(prompt):
    print('+' + '-'*(len(prompt)) + '--+')
    print('|' + ' '*(len(prompt)) + '  |')
    print(f'| {prompt} |')
    print('|' + ' '*(len(prompt)) + '  |')
    print('+' + '-'*(len(prompt)) + '--+')

print_in_box('To boldy go where no one hs gone before')
print_in_box('')