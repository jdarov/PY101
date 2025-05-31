#solution 1
def is_color_valid(color):
    return color == 'blue' or color == 'green'

print(is_color_valid('blue')) 
print(is_color_valid('red'))

#solution 2
def is_color_valid(color):
    return color in {'blue', 'green'}

print(is_color_valid('blue')) 
print(is_color_valid('red'))
    
