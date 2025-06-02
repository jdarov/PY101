def crunch(string):
    if not string:
        return ''
    
    new_string = [string[0]]
    
    for char in string[1:]:
        if char != new_string[-1]:
            new_string.append(char)
    
    return ''.join(new_string)


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')