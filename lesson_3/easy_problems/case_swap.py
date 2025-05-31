munsters_description = "The Munsters are creepy and spooky."
case_swap = []
for char in munsters_description:
    if char.isupper():
        case_swap.append(char.lower())
    else:
        case_swap.append(char.upper())

print(''.join(case_swap))
print(munsters_description.swapcase())