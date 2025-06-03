def clean_up(dirty_string):
    repeat_punc = False
    good_list = []
    for char in dirty_string:
        if not char.isalpha() and repeat_punc:
            continue
        if (not char.isalpha()) and (not repeat_punc):
            good_list.append(' ')
            repeat_punc = True
            continue
        if char.isalpha() or char.isspace():
            good_list.append(char)
            repeat_punc = False
            continue
    return ''.join(good_list)


print(clean_up("---what's my +*& line?") == " what s my line ")
# True



