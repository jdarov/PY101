def triangle(sides):
    return '\n'.join([('*'*n).rjust(sides) for n in range(1, sides+1)])

print(triangle(6))
# print('    *')
# print('   **')
# print('  ***')
# print(' ****')
# print('*****')