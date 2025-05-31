def center_of(string):
    center_index = len(string)//2
    if len(string) % 2 == 0:
        return string[center_index-1] + string[center_index]
    return string[center_index]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True